# The Heritage Signature Score

### Louis Vuitton, 1854–2025

*Can structural form signal a house identity without the Monogram?*

**Nijat Shikhaliyev** · Independent research

**[Read the research report (PDF)](Heritage_Signature_Score_Research_Report.pdf)** · [Interactive Louis Vuitton Heritage Atlas](https://louis-vuitton-beryl.vercel.app/)

---

## Research question

Louis Vuitton is among the world's most recognisable houses, and its identity is often associated with the Monogram canvas introduced in 1896. This study asks whether an object's form carries recognisable information even when branding is removed. If an object were reduced to a black silhouette, would it still be identified as Louis Vuitton?

## Method

### Catalogue and feature ratings

The catalogue contains **400 Louis Vuitton objects dated 1854–2025**. Each object was coded on eight visible features using a written 1–5 rating scale, then normalised to the interval [0, 1].

| Feature | Definition |
|---|---|
| `rigidity` | Stiffness of the body |
| `edge_straightness` | Straightness of outline edges |
| `geometry` | Reduction to simple geometric forms |
| `symmetry` | Vertical mirror symmetry |
| `ornament_density` | Share of patterned surface |
| `ornament_regularity` | Periodicity of pattern |
| `hardware` | Count of visible metal elements |
| `travel_function` | Role in carrying goods while travelling |

### S8 and S6

The historical reference vector is the feature-wise median of the **124 catalogue objects dated 1854–1949** (107 of them trunks). If *x<sub>j</sub>* is an object's normalised score for a feature and *m<sub>j</sub>* its historical median, the score over *k* included features is

**S = 1 − (1 / k) Σ |x<sub>j</sub> − m<sub>j</sub>|**

S = 1 represents an exact match to the historical median profile and S = 0 represents maximum mean deviation.

- **S8** uses all eight normalised features.
- **S6** removes `ornament_density` and `ornament_regularity`, so that the score does not incorporate surface-pattern information.

### Recognition survey

The recognition survey involved **3,000 participants across Azerbaijan, Georgia, London, and the San Francisco Bay Area**. It presented **30 black silhouettes**: 20 Louis Vuitton objects and ten objects from Goyard, Moynat, Au Départ, Globe-Trotter, Innovation, Hermès and Bottega Veneta. Each silhouette was assessed by 100 participants, who answered the question *"Is this a Louis Vuitton object?"* The analyses use the 30 stimulus-level aggregate counts.

## Principal results

### The score over time (trunks)

| Period | Catalogue objects | Trunks | S8, trunks | S6, trunks |
|---|---:|---:|---:|---:|
| 1854–1899 | 43 | 42 | 0.985 | 0.980 |
| 1900–1949 | 81 | 65 | 0.816 | 0.975 |
| 1950–1999 | 133 | 47 | 0.765 | 0.969 |
| 2000–2025 | 143 | 34 | 0.738 | 0.938 |

### Score and recognition (Pearson correlations)

| Subset | n | S8 r | S8 p | S6 r | S6 p |
|---|---:|---:|---:|---:|---:|
| All silhouettes | 30 | −0.076 | 0.688 | +0.434 | 0.017 |
| Louis Vuitton only | 20 | −0.001 | 0.995 | +0.505 | 0.023 |
| Non-iconic objects | 19 | +0.117 | 0.634 | +0.569 | 0.011 |
| LV, non-iconic only | 9 | +0.132 | 0.734 | +0.685 | 0.042 |

Across the 20 Louis Vuitton stimuli the mean affirmative rate was 51.35%, compared with 30.6% for the ten control-brand stimuli.

### Regression and sensitivity analyses

| Model | Sample and method | Result |
|---|---|---|
| A | 400 objects · OLS, HC3 robust SE · S6 on year, category, iconic status | Iconic model +0.013, p = 0.289 · R² = 0.725 |
| B | 30 stimuli · quasi-binomial GLM · S6, category, brand | S6 +2.477, p = 0.228 |
| C | 20 Louis Vuitton stimuli · quasi-binomial GLM · S6, category, iconic status, year | S6 +3.983, p = 0.122 · year +0.144 per decade, p = 0.095 |
| D | 12 trunk stimuli · quasi-binomial GLM · S6, brand | S6 +9.882, p = 0.142 · bivariate r = +0.488, p = 0.108 |

These results support an exploratory, correlational finding rather than a demonstrated independent effect of structural form.

## Data and analysis files

| File | Contents |
|---|---|
| [`Heritage_Signature_Score_Research_Report.pdf`](Heritage_Signature_Score_Research_Report.pdf) | Research report, revised November 2026, with its revision history |
| [`LV_Heritage_Signature_Score.xlsx`](LV_Heritage_Signature_Score.xlsx) | Research workbook (see sheets below) |
| [`model_A_analysis.py`](model_A_analysis.py) | Model A; writes `modelA_full400.csv` (coefficients) and `modelA_full400_data.csv` (model input) |
| [`models_BC_analysis.py`](models_BC_analysis.py) | Models B and C; writes `modelB_quasi.csv`, `modelC_quasi.csv` and `regression_data.csv` (model input) |
| `modelA_full400.csv`, `modelA_full400_data.csv`, `modelB_quasi.csv`, `modelC_quasi.csv` | Model outputs as reported |
| [`archive/`](archive/) | Earlier versions kept for provenance: the September 2026 report, the November 2026 correction notice and earlier regression notes |

Workbook sheets:

| Sheet | Contents |
|---|---|
| `1_METHOD` | Summary of the method |
| `2_SCALES` | Written 1–5 definitions of the eight features |
| `3_OBJECTS` | The 400 catalogued objects: sources, ratings, normalised values, S8 and S6 |
| `4_BENCHMARK` | Historical reference profile (1854–1949) and 2000–2025 medians |
| `5_TIMELINE` | Scores by decade and by period, for all objects and for trunks |
| `6_SURVEY` | The 30 recognition stimuli: ratings, S8, S6 and aggregate recognition counts |
| `7_RESULTS` | Summary correlations |
| `8_COVERAGE` | Catalogue composition by decade and object type |

To reproduce Models A–C:

```bash
pip install pandas numpy scipy statsmodels openpyxl
python model_A_analysis.py
python models_BC_analysis.py
```
