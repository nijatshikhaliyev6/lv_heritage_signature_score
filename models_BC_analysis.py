import openpyxl, re
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

wb = openpyxl.load_workbook('LV_Heritage_Signature_Score__4_.xlsx', data_only=True)
ws = wb['6_SURVEY']

CATEGORY = {
 1:'trunk',2:'trunk',3:'trunk',4:'trunk',5:'trunk',6:'trunk',
 7:'box',8:'box',9:'box',10:'trunk',11:'bag',12:'trunk',13:'bag',
 14:'bag',15:'bag',16:'bag',17:'bag',18:'suitcase',19:'box',20:'box',
 21:'trunk',22:'trunk',23:'trunk',24:'suitcase',25:'trunk',
 26:'bag',27:'bag',28:'bag',29:'bag',30:'bag',
}

rows = []
for r in range(5, 35):
    n = ws.cell(r, 1).value
    if n is None: continue
    name = ws.cell(r, 2).value
    brand = ws.cell(r, 3).value
    iconic = ws.cell(r, 4).value
    S6 = ws.cell(r, 30).value
    shown = ws.cell(r, 22).value
    answered = ws.cell(r, 23).value
    m = re.search(r'\b(1[89]\d{2}|20[0-2]\d)\b', str(name))
    year = int(m.group(1)) if m else None
    if n == 1: iconic = 'yes'
    rows.append(dict(n=n, name=name, brand=brand, iconic=iconic, S6=S6,
                      category=CATEGORY[n], year=year, shown=shown, answered=answered))

df = pd.DataFrame(rows)
df['iconic_bin'] = (df['iconic'] == 'yes').astype(int)
df['is_lv'] = (df['brand'] == 'LV').astype(int)
df['successes'] = df['answered']
df['failures'] = df['shown'] - df['answered']

def fit_quasi_manual(endog, exog, label, df_extra=None):
    """Fit binomial GLM, then manually apply quasi-likelihood overdispersion
    correction: SE_adj = SE_raw * sqrt(pearson_chi2 / df_resid).
    This is the standard quasi-binomial correction (equivalent to R's
    family=quasibinomial), applied by hand because statsmodels' built-in
    scale='X2' option misestimates dispersion for grouped binomial data
    with a constant number of trials per row (a known edge case)."""
    m = sm.GLM(endog, exog, family=sm.families.Binomial())
    r = m.fit()
    disp = r.pearson_chi2 / r.df_resid
    se_adj = r.bse * np.sqrt(disp)
    z_adj = r.params / se_adj
    p_adj = 2 * (1 - stats.norm.cdf(np.abs(z_adj)))
    ci_lo = r.params - 1.96 * se_adj
    ci_hi = r.params + 1.96 * se_adj

    table = pd.DataFrame({
        'coef': r.params, 'se': se_adj, 'z': z_adj, 'p': p_adj,
        'ci_lo': ci_lo, 'ci_hi': ci_hi
    })

    null_exog = np.ones((len(endog), 1))
    null_r = sm.GLM(endog, null_exog, family=sm.families.Binomial()).fit()
    mcfadden_r2 = 1 - r.llf / null_r.llf

    print(f'\n{"="*74}\n{label}\n{"="*74}')
    print(f'n = {len(endog)}, df_resid = {r.df_resid}, dispersion (Pearson chi2/df) = {disp:.2f}')
    print(f'McFadden pseudo-R2 = {mcfadden_r2:.3f}')
    print(table.round(4).to_string())
    return table, disp, mcfadden_r2

print('MODEL A — All 30 stimuli: S6 + category (ref: bag) + brand (LV vs control)')
endog_A = df[['successes','failures']].values
exog_A = pd.get_dummies(df[['S6','category','is_lv']], columns=['category'], drop_first=True).astype(float)
exog_A = sm.add_constant(exog_A)
exog_A.columns = ['const','S6','is_lv','category_box','category_suitcase','category_trunk']
exog_A = exog_A[['const','S6','category_box','category_suitcase','category_trunk','is_lv']]
tA, dispA, r2A = fit_quasi_manual(endog_A, exog_A, 'MODEL A')

print('\nMODEL B — Louis Vuitton objects only (n=20): S6 + category + iconic + year')
dflv = df[df['is_lv']==1].copy()
dflv['year_c'] = (dflv['year'] - dflv['year'].mean()) / 10
endog_B = dflv[['successes','failures']].values
exog_B = pd.get_dummies(dflv[['S6','category','iconic_bin','year_c']], columns=['category'], drop_first=True).astype(float)
exog_B = sm.add_constant(exog_B)
exog_B.columns = ['const','S6','iconic_bin','year_c','category_box','category_suitcase','category_trunk']
exog_B = exog_B[['const','S6','category_box','category_suitcase','category_trunk','iconic_bin','year_c']]
tB, dispB, r2B = fit_quasi_manual(endog_B, exog_B, 'MODEL B')

tA.to_csv('modelA_quasi.csv')
tB.to_csv('modelB_quasi.csv')
df.to_csv('regression_data.csv', index=False)
print('\nSaved modelA_quasi.csv, modelB_quasi.csv, regression_data.csv')
