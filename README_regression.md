# Regression analysis — reproducibility notes

This folder contains the full data and code behind Section 7 ("Robustness check")
of the Heritage Signature Score report.

## Files

- `regression_data.csv` — the 30 survey stimuli with all variables used in the
  regression: S6 score, category (trunk/suitcase/bag/box), brand (LV vs. control),
  iconic status, production year (Louis Vuitton objects only), and the raw
  recognition counts (`answered` out of `shown` = 100 respondents per stimulus).
- `regression_analysis.py` — the full analysis script. Running it reproduces
  every coefficient, standard error, and p-value reported in the PDF report,
  starting only from `regression_data.csv`.
- `modelA_quasi.csv`, `modelB_quasi.csv` — the fitted regression tables as
  exported directly by the script.

## Method, briefly

Each of the 30 stimuli was shown to an independent cohort of 100 respondents,
so the outcome for each stimulus is a count of successes out of 100 trials —
not a continuous percentage. This is modelled with a binomial GLM (logistic
regression on grouped counts).

An initial fit showed substantial overdispersion (Pearson χ²/df ≈ 25, versus
an expected value of 1 for a well-specified binomial model). Left uncorrected,
this understates standard errors and overstates significance. A standard
quasi-likelihood correction is applied by hand: standard errors from the raw
binomial fit are scaled by the square root of the estimated dispersion before
p-values are computed. This is equivalent to R's `family = quasibinomial()`.

Note: `statsmodels`' built-in `scale='X2'` option was tested and found to
misestimate dispersion by a factor of 100 for this specific data shape — a
grouped binomial outcome with an identical number of trials (100) in every
row. The script includes the manual correction as a result, with the
discrepancy documented in the code comments.

## Reproducing the result

```bash
pip install pandas numpy scipy statsmodels
python3 regression_analysis.py
```

This prints both models' full coefficient tables, standard errors, and
p-values to the console, and re-saves the CSV outputs.
