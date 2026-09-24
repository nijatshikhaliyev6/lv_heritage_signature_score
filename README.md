# Heritage Signature Score — Louis Vuitton, 1854–2025

### Can the form of a Louis Vuitton object carry the identity of the House independently of the Monogram?

**Independent research by Nijat Shikhaliyev**

This repository contains the data, methodology, scoring framework, survey results, and reproducible analyses for the **Heritage Signature Score**, a quantitative study of Louis Vuitton's visual and structural design language from 1854 to 2025.

The study examines **400 catalogued Louis Vuitton objects spanning 170 years** and tests whether structural form alone — without the Monogram, Damier canvas, colour, material, or visible branding — is associated with recognition as Louis Vuitton.

A separate recognition experiment used **30 black silhouettes and 3,000 independent respondent-stimulus observations** to test whether objects that remain structurally closer to the House's historical design language are more likely to be identified as Louis Vuitton.

---

## Research Question

Louis Vuitton is one of the world's most recognizable luxury houses, but much of that recognition is commonly associated with its surface codes, particularly the Monogram canvas introduced in 1896.

This study asks a narrower question:

> **If the Monogram were removed — if an object were reduced to its form — would it still be identifiable as Louis Vuitton?**

To investigate this, the study develops a quantitative **Heritage Signature Score (HSS)** measuring how closely an object's visual structure corresponds to Louis Vuitton's historical design profile.

---

## Dataset

The catalogue contains **400 Louis Vuitton objects produced between 1854 and 2025**.

Each object is independently described using eight visual features scored from 1 to 5:

| Feature | What it measures |
|---|---|
| `rigidity` | Whether the object holds its shape when empty |
| `edge_straightness` | Straightness of the body's edges |
| `geometry` | Whether the outline reduces to a simple geometric figure |
| `symmetry` | Mirror symmetry around the vertical axis |
| `ornament_density` | Share of the surface covered by repeating pattern |
| `ornament_regularity` | Regularity of the repeating pattern |
| `hardware` | Number of visible metal elements |
| `travel_function` | Degree to which the object is designed for carrying goods |

All ratings use predefined written criteria reproduced in the research report.

---

## The Heritage Signature Score

The historical reference profile is defined as the median feature profile of the **124 objects produced between 1854 and 1949**.

For an object with normalized feature vector `x` and historical reference vector `r`:

**S = 1 − mean(|x − r|)**

where:

- **S = 1** represents an exact match to the historical reference profile
- **S = 0** represents maximum possible deviation

Two versions of the score are calculated.

### S8 — Full Heritage Signature Score

Uses all eight features, including ornament.

### S6 — Structural Heritage Signature Score

Removes:

- `ornament_density`
- `ornament_regularity`

S6 therefore measures structural similarity independently of repeating surface ornament and is the primary index used to test whether form itself carries recognizable House identity.

---

## Recognition Experiment

Thirty objects were converted into black silhouettes:

- **20 Louis Vuitton objects**, dating from 1860 to 2023
- **10 control objects** from other houses and luggage manufacturers

The control set includes objects from Goyard, Moynat, Au Départ, Globe-Trotter, Innovation, Hermès, and Bottega Veneta.

Respondents saw one silhouette and answered a single question:

> **Is this a Louis Vuitton object?**

Each silhouette was evaluated by an **independent cohort of 100 respondents**.

No respondent evaluated more than one stimulus.

The resulting experiment therefore contains:

**30 stimuli × 100 respondents = 3,000 independent respondent-stimulus observations**

---

## Main Results

### 1. Structural continuity across 170 years

When the analysis is restricted to trunks — the only object category represented continuously across the full historical period — the structural score remains remarkably stable:

| Period | S6 | S8 |
|---|---:|---:|
| 1854–1899 | 0.980 | 0.985 |
| 1900–1949 | 0.975 | 0.816 |
| 1950–1999 | 0.969 | 0.765 |
| 2000–2025 | 0.937 | 0.738 |

Across approximately 170 years, S6 declines only modestly, while S8 declines substantially.

**The structure held. The surface changed.**

---

### 2. Structural similarity is associated with recognition

Across all 30 survey silhouettes:

**S6 → recognition:**  
`r = +0.434, p = 0.017`

**S8 → recognition:**  
`r = −0.076, p = 0.688`

The structural score therefore shows a positive bivariate association with recognition in the present stimulus sample, whereas the full score including ornament does not.

---

### 3. The association strengthens among non-iconic models

For the 18 non-iconic objects:

**S6 → recognition:**  
`r = +0.573, p = 0.013`

For the eight non-iconic Louis Vuitton objects:

**S6 → recognition:**  
`r = +0.716, p = 0.046`

The final subset is small and should therefore be interpreted cautiously.

---

## Controlled Analyses

The repository also contains four robustness models designed to test alternative explanations for the observed relationship.

### Model A — Full 400-object catalogue

OLS model predicting S6 from:

- production year
- object category
- iconic status

`n = 400`

`R² = 0.725`

Iconic status was not significantly associated with S6 after controlling for category and year (`p = 0.289`), suggesting that the structural index is not simply measuring model fame.

### Model B — All survey stimuli

Quasi-binomial recognition model controlling for:

- S6
- category
- Louis Vuitton/control status

`n = 30`

The S6 coefficient remained positive but was not statistically significant:

`β = +2.477, p = 0.228`

### Model C — Louis Vuitton objects only

Controls for:

- S6
- category
- iconic status
- production year

`n = 20`

S6 again remained positive but did not reach the conventional significance threshold:

`β = +4.129, p = 0.100`

### Model D — Trunks only

Holding category constant by restricting the sample to trunks:

`r = +0.488, p = 0.108` for LV + control trunks

`r = +0.325, p = 0.432` for Louis Vuitton trunks only

These controlled analyses substantially narrow the interpretation of the bivariate findings. The present data support a **consistently positive but statistically inconclusive independent association** once category and brand are accounted for.

---

## Inter-Rater Reliability

To test whether the scoring framework could be reproduced independently, a **stratified random sample of 100 of the 400 objects (25%)** was re-coded by a second rater.

The second rater:

- used the same written definitions
- worked independently
- received no additional scoring instruction
- was blinded to the original ratings

Reliability was evaluated using **ICC(2,1)** and weighted Cohen's κ.

Feature-level ICCs ranged from:

`0.87 – 0.96`

Composite-score reliability was:

| Index | ICC(2,1) |
|---|---:|
| S6 | **0.980** |
| S8 | **0.986** |

These results indicate high reproducibility of the scoring framework.

---

## Interpretation

The study does **not** claim that structural form causes Louis Vuitton recognition.

Instead, it establishes a narrower result:

> Within the present silhouette sample, objects structurally closer to Louis Vuitton's historical design profile tended to receive higher Louis Vuitton recognition rates after visible branding was removed.

The bivariate relationship is statistically significant, but the controlled models do not establish an independent S6 effect once category, brand, iconic status, and year are considered.

The Heritage Signature Score should therefore be understood primarily as a **measurement instrument** for quantifying continuity and change in design language.

---

## Repository Contents

This repository contains the materials required to inspect, reproduce, and extend the study, including:

- the 400-object catalogue
- object-level feature ratings
- source links
- historical reference-profile calculations
- S6 and S8 calculations
- recognition-survey data
- survey stimuli
- inter-rater reliability data
- statistical analyses
- figures and tables used in the final report

See the individual folders and files for documentation of each component.

---

## Reproducibility

The scoring rules were fixed before the recognition survey was conducted.

The eight features, historical reference period, S6/S8 definitions, and scoring formula were not altered after survey results were observed.

The repository is intended to make the study auditable: the reported tables and figures can be reconstructed from the underlying data.

---

## Limitations

The recognition experiment contains only 30 stimuli, limiting statistical power in controlled and subset analyses.

The historical reference profile is heavily composed of trunks because trunks dominate Louis Vuitton's pre-1950 output.

Black silhouettes remove not only branding but also colour, material, texture, and hardware finish.

Survey respondents were recruited opportunistically rather than through a representative population sampling frame.

Accordingly, the recognition results should not be interpreted as population-level estimates or as causal evidence.

---

## Heritage Atlas

The dataset can also be explored through the interactive **Louis Vuitton Heritage Atlas**, which presents the catalogue across objects and decades.

**Heritage Atlas:**  
https://louis-vuitton-beryl.vercel.app

---

## Citation

If you use the dataset, scoring framework, or results in academic or design research, please cite:

> **Shikhaliyev, Nijat. (2026). _The Heritage Signature Score: Louis Vuitton, 1854–2025._ Independent Research.**

---

## Author

**Nijat Shikhaliyev**  
Independent Researcher  
Baku, Azerbaijan

---

## Disclaimer

This is an independent academic research project.

It is not affiliated with, commissioned by, or endorsed by Louis Vuitton, LVMH, or any of the other brands represented in the comparative dataset.

All trademarks and brand names remain the property of their respective owners.
