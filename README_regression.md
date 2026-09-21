# Regression analysis — reproducibility notes

This folder contains the full data and code behind Section 7 ("Robustness check:
three regression models") of the Heritage Signature Score report.

## Models

**Model A** — what predicts the structural score (S6) itself?
OLS regression, S6 ~ year + type + iconic status, across **all 400 rated objects**
in the catalogue (not just the 30 survey stimuli). Heteroskedasticity-robust
(HC3) standard errors. This is the primary robustness check: it confirms that
S6 tracks object form and era, not fame — iconic status has no significant
effect (p = 0.289) once year and type are controlled for.

**Model B** — does S6 predict recognition, controlling for category and brand?
Binomial GLM (logistic regression on grouped counts) on the 30 survey stimuli,
with a manual quasi-likelihood correction for overdispersion (see below).

**Model C** — same as B, restricted to the 20 Louis Vuitton stimuli, adding
control for iconic status and production year.

## Files

- `modelA_full400_data.csv` — all 400 objects with S6, S8, year, type, and
  iconic status, as used in Model A
- `modelA_full400.csv` — Model A's fitted coefficient table
- `model_A_analysis.py` — script that reproduces Model A from the raw workbook
- `regression_data.csv` — the 30 survey stimuli with S6, category, brand,
  iconic status, year (LV objects), and raw recognition counts, as used in
  Models B and C
- `modelB_quasi.csv`, `modelC_quasi.csv` — Models B and C's fitted tables
- `models_BC_analysis.py` — script that reproduces Models B and C

## Method notes

**Model A** uses ordinary least squares because S6 is a continuous 0–1 score
computed from eight rated features, and n = 400 is large enough for standard
inference. Robust (HC3) standard errors are used because the residuals show
non-normal skew, which OLS's default assumption does not accommodate well.

**Models B and C** use a binomial GLM because the outcome for each stimulus is
a count of successes out of 100 independent trials — not a continuous
percentage. An initial fit showed substantial overdispersion (Pearson
chi-square / degrees of freedom ≈ 25, versus an expected ≈ 1). Left
uncorrected, this understates standard errors and overstates significance. A
standard quasi-likelihood correction is applied by hand: raw binomial standard
errors are scaled by the square root of the estimated dispersion before
p-values are computed — equivalent to R's `family = quasibinomial()`.

Note: `statsmodels`'s built-in `scale='X2'` option was tested and found to
misestimate dispersion by a factor of 100 for this specific data shape (a
grouped binomial outcome with an identical number of trials — 100 — in every
row). The manual correction avoids this issue; see comments in
`models_BC_analysis.py`.

## Reproducing the results

```bash
pip install pandas numpy scipy statsmodels openpyxl
python3 model_A_analysis.py
python3 models_BC_analysis.py
```

Both scripts read directly from `LV_Heritage_Signature_Score.xlsx` and print
full coefficient tables, standard errors, and p-values to the console.
