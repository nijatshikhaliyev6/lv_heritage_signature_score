# Correction notice

## The Heritage Signature Score: Louis Vuitton, 1854–2025

Nijat Shikhaliyev · Notice dated 24 November 2026

Applies to the report *The Heritage Signature Score* (file `Heritage_Signature_Score_Final.pdf`, 15 pages, dated 24 September 2026). The report itself has not been altered. This notice should be read together with it.

### 1. Summary

One survey stimulus, object #131 (a circa-1860 Gris Trianon canvas trunk), was coded inconsistently as iconic or non-iconic across the study's files. In the corrected files released with this notice, object #131 is classified as non-iconic, and all affected results have been recomputed. The original report is unchanged, and the previously released data and code remain available in the repository's version history.

The changes are small, with one exception: the report stated that production year was a statistically significant predictor of recognition among Louis Vuitton objects (Model C). After correction, the year coefficient is not statistically significant at the 0.05 level (p = 0.095), and that statement is withdrawn.

The report's overall conclusion is unchanged: a positive association between the structural score S6 and recognition that is not statistically established once category, brand, iconic status and year are controlled.

### 2. What was inconsistent

Object #131 is described in its source (a Christie's lot) as *A Gris Trianon coated canvas trunk with black lacquered iron & brass hardware*, circa 1860. It is catalogue object 131 and survey stimulus 1. Its iconic status was recorded as follows in the materials released in September 2026:

| Where | Coded as |
|---|---|
| Catalogue sheet of the workbook (`3_OBJECTS`, cell H135) | iconic |
| Survey sheet of the workbook (`6_SURVEY`, cell D5) | non-iconic |
| Survey analysis script (`models_BC_analysis.py`), which set stimulus 1 to iconic | iconic |
| Input data for Model A (`modelA_full400_data.csv`) | non-iconic |
| Report, Figures 2 and 3 and Appendix B | iconic |

As a result, the report's non-iconic subset correlations and Model C treated #131 as iconic, while Model A treated it as non-iconic. The study's files do not record why the catalogue value and the script setting were chosen.

### 3. Decision and its basis

In the corrected files released with this notice, object #131 is consistently classified as non-iconic. The files released in September 2026 remain available in the repository's version history. This decision was made on 24 November 2026, after the recognition survey had been conducted and after the results were first published. It was not specified in advance.

The basis is consistency with the coding of comparable objects. The report defines "iconic" as "a distinctive Louis Vuitton model, design family, or historically established named form with a recognised identity within the House's design history" (Section 2.4).
- **The source title names no model.** It describes #131 only by its canvas and hardware.
- **All comparable trunks are non-iconic.** The catalogue contains nine other Gris (grey) Trianon canvas trunks, dated 1860–1888: objects 66, 77, 107, 191, 249, 267, 268, 269 and 270. All nine are coded non-iconic.
- **Nothing on record separates #131 from them.** No record identifies a characteristic that would justify coding #131 differently.

This written definition of "iconic" first appeared in the final version of the report. Earlier drafts described non-iconic objects as those with "no famous name attached".

No other object's classification has been changed. No feature ratings, scores or survey responses have been changed. Results under both codings are given below so that readers can judge the effect of the decision.

### 4. Corrections to the report, page by page

Values in the "As published" column are quoted from the report. Corrected values are computed from the corrected workbook and analysis script.

| Page | Location | As published | Corrected |
|---|---|---|---|
| 1 | Summary of findings, item 3 | "the six-feature correlation rises to r = +0.573 (p = 0.013)" | "the six-feature correlation rises to r = +0.569 (p = 0.011)" |
| 1 | Summary of findings, item 4 | Model C: "not statistically significant (p = 0.100)" | "not statistically significant (p = 0.122)" |
| 1 | Summary table, row "Non-iconic models only" | n = 18; S8 r = +0.105 (p = 0.679); S6 r = +0.573 (p = 0.013) | n = 19; S8 r = +0.117 (p = 0.634); S6 r = +0.569 (p = 0.011) |
| 6 | Section 5.2, results table, row "Non-iconic models only" | n 18; S8 +0.105, p 0.679; S6 +0.573, p 0.013 | n 19; S8 +0.117, p 0.634; S6 +0.569, p 0.011 |
| 6 | Section 5.2, results table, row "LV, non-iconic only" | n 8; S6 +0.716, p 0.046 | n 9; S6 +0.685, p 0.042 |
| 7 | Paragraph above Figure 2 | "to r = +0.573 among non-iconic models, and reaches r = +0.716 (p = 0.046) in the eight-object subset of non-iconic Louis Vuitton models" | "to r = +0.569 among non-iconic models, and reaches r = +0.685 (p = 0.042) in the nine-object subset of non-iconic Louis Vuitton models" |
| 7 | Same paragraph | "Model C (p = 0.100)" | "Model C (p = 0.122)" |
| 7 | Figure 2 | See Section 5 of this notice | See Section 5 of this notice |
| 9 | Section 7.3, Model C table | See the table below | See the table below |
| 9 | Line below the Model C table | "n = 20, dispersion = 22.5, McFadden pseudo-R2 = 0.51" | "n = 20, dispersion = 23.1, McFadden pseudo-R2 = 0.50" |
| 9 | Text below the Model C table | "Here S6 is larger and closer to conventional significance (p = 0.100)" | "Here S6 is larger and closer to conventional significance (p = 0.122)" |
| 9 | Text below the Model C table | "Year itself is a significant predictor within this subset: more recent Louis Vuitton objects are recognised at higher rates independent of S6, iconic status, or category." | Withdrawn. Replace with: "Year is positively associated with recognition within this subset (β = +0.144 per decade), but the association is not statistically significant at the 0.05 level (p = 0.095)." |
| 15 | Appendix B, text | "an iconic pre-Monogram trunk" | "a non-iconic pre-Monogram trunk" |
| 15 | Figure 3, label under "1860 Trianon Trunk" | "Louis Vuitton, iconic · S6 = 1.00 · 41% recognised" | "Louis Vuitton, non-iconic · S6 = 1.00 · 41% recognised" |

**Section 7.3, Model C (Louis Vuitton objects only, n = 20), quasi-binomial GLM**

| Term | As published: coef. (SE), z, p | Corrected: coef. (SE), z, p |
|---|---|---|
| S6 | +4.129 (2.507), 1.65, 0.100 | +3.983 (2.576), 1.55, 0.122 |
| Category: box | +0.782 (0.831), 0.94, 0.347 | +0.742 (0.838), 0.88, 0.376 |
| Category: suitcase | +2.158 (1.358), 1.59, 0.112 | +1.992 (1.340), 1.49, 0.137 |
| Category: trunk | +1.451 (1.298), 1.12, 0.263 | +1.245 (1.251), 0.99, 0.320 |
| Iconic model | +1.031 (0.578), 1.78, 0.075 | +0.991 (0.590), 1.68, 0.093 |
| Year (per decade, centred) | +0.187 (0.089), 2.10, 0.035 | +0.144 (0.086), 1.67, 0.095 |

### 5. Figures

This notice does not reissue any figure. The required changes are described here instead.

- **Figure 2 (page 7).** The point for #131 (S6 = 1.00, 41% recognised) is drawn as a filled marker, which the legend defines as an iconic Louis Vuitton model. Its annotation reads "1860 Trianon trunk (iconic, earliest object in the survey)". The marker should be open (non-iconic) and the annotation should read "(non-iconic, earliest object in the survey)". No point moves. The fitted line and the reported r = +0.434 (p = 0.017) are unchanged.
- **Figure 3 (page 15).** The label under "1860 Trianon Trunk" should read "Louis Vuitton, non-iconic", as given in Section 4. The silhouette, S6 value and recognition rate are unchanged.
- **Figure 1 (page 6)** does not involve iconic status and is unaffected.

### 6. Effect on conclusions

- **Summary item 3 and Section 5.2 still hold.** The association between S6 and recognition is stronger in the non-iconic subset (r = +0.569, n = 19) than across all 30 stimuli (r = +0.434). In the non-iconic Louis Vuitton subset it is r = +0.685 (p = 0.042, n = 9). This subset remains small, and the result should be treated as indicative rather than definitive.
- **Summary item 4 and Section 7 still hold.** In Model C the S6 coefficient remains positive and not statistically significant (p = 0.122).
- **The Section 7.3 statement that year is a significant predictor is withdrawn** (p = 0.095).

### 7. Results not affected

The following do not depend on the classification of #131 and are unchanged:
- the trunk timeline and Figure 1;
- the correlations across all 30 stimuli (S6 r = +0.434, p = 0.017; S8 r = −0.076, p = 0.688);
- the correlations for Louis Vuitton objects only (S6 r = +0.505, p = 0.023; S8 r = −0.001, p = 0.995);
- Model B (S6 p = 0.228) and Model D.

Model A (iconic status p = 0.289; R² = 0.725) is also unchanged, because its input data already coded #131 as non-iconic.

### 8. Changes to the data and code

- `LV_Heritage_Signature_Score.xlsx`: in the `3_OBJECTS` sheet, cell H135 changed from "yes" to "no". No other cell was changed.
- `models_BC_analysis.py`: removed the line that set survey stimulus 1 to iconic. The script now uses the value in the survey sheet, which matches the catalogue.
- `modelC_quasi.csv`: regenerated from the corrected workbook and script.
