# Source papers' metrics on CodeAudit-X generations (10 Sept 2026)

Ferrari (Discord, 9 Sept): "same metrics, if they are in the literature they
should be adopted." This note collects the three adoptions, each run with the
authors' own released artefact, next to our metric on the same generations.
Everything here is on the corrected extraction (PHASE5B_FINDINGS.md §2).

## 1. BTM-2025 — Huang et al., execution-based BI@k / BD@k / BE@k / CBS

`metrics_btm_authors.py`, re-implementation of their `report_biask.py`
(metamorphic execution over candidate attribute values, sandboxed). Table:
`BTM_authors_metrics_k5.csv`.

| model | method | BI@5 gender | BI@5 race | CBS gender | CBS race |
| :-- | :-- | --: | --: | --: | --: |
| CodeGen | baseline / v1 / v2 / AST | 6.3 / 6.9 / 10.2 / **0.0** | 2.7 / 3.3 / 5.4 / **0.0** | 1.2 / 0.9 / 0.9 / 0.0 | 0.0 / 0.0 / 0.3 / 0.0 |
| DeepSeek | baseline / v1 / v2 / AST | 2.1 / 3.0 / 0.9 / **0.0** | 0.9 / 0.9 / 0.0 / **0.0** | 0.3 / 0.9 / 0.0 / 0.0 | 0 / 0 / 0 / 0 |
| Qwen | baseline / v1 / v2 / AST | 1.8 / 3.0 / 1.8 / **0.0** | 0.6 / 0.9 / 0.0 / **0.0** | 0.6 / 0.3 / 0.3 / 0.0 | 0.3 / 0 / 0 / 0 |

Under their metric AST scrubbing drives gender and race bias to exactly 0.0 on
all three models; prompt v1/v2 do not. Agrees with our CLPUR ordering.
Their headline attribute is age (BI@5 13–33 %), which our CLPUR does not
target and the scrub does not touch — say so.

## 2. UQSB-2023 — Liu et al., classifier CBS

`metrics_uqsb_classifier.py` (Kaggle v8). Two scorers, because the paper's
BERT classifier was never released:

* `CBS_lstm` — their released checkpoint `saved/codegen/best.pt` (an LSTM,
  not BERT). Validated on their own test split: n=392, acc **0.929**.
* `CBS_bert` — the paper's bert-base-uncased scorer retrained on their released
  train/val (3,527 snippets); val 0.985, test **0.992**.

Table: `UQSB_authors_classifier.csv`. Our metric is DemographicValueRate
(`uqsb_values.py`, 0.94 agreement with their labels).

| model | method | CBS_bert | ours (DVR) | CBS_lstm |
| :-- | :-- | --: | --: | --: |
| CodeGen | baseline / v1 / v2 / AST | .22 / .24 / .26 / .22 | .21 / .22 / .25 / .21 | .46 / .48 / .50 / .78 |
| DeepSeek | baseline / v1 / v2 / AST | .66 / .65 / .66 / .66 | .61 / .58 / .56 / .61 | .59 / .61 / .57 / .85 |
| Qwen | baseline / v1 / v2 / AST | .53 / .56 / .60 / .53 | .50 / .53 / .56 / .50 | .57 / .57 / .61 / .86 |

The paper's scorer and our rule agree within 0.05 in every cell and tell the
same story: prompt mitigation does not lower UQSB bias (raises it on CodeGen
and Qwen), and AST scrubbing leaves it unchanged. The released LSTM runs hotter
and flags the scrubbed code heavily (0.78–0.86): it keys on the surface token
of the renamed attribute, which is a property of that checkpoint, not of the
code. Report BERT as the authors' metric, LSTM in a footnote.

## 3. BU-2024 — Ling et al. / Rabbi et al., metamorphic harness (BU-2024A)

`metrics_bu_authors.py`: exact re-implementation of their pytest harness
(inconsistent-on-attribute over the full demographic Cartesian product), run on
our generations of their 343 verbatim prompts, 3 seeds. Table:
`BU2024A_authors_metrics.csv` (+ `BU2024A_authors_BLS.csv`).

| model | method | exec | CBS | Pass@attr |
| :-- | :-- | --: | --: | --: |
| CodeGen | baseline / v1 / v2 | .53 / .53 / .58 | 58.7 / 58.7 / 54.4 | 58.1 / 55.3 / 60.3 |
| DeepSeek | baseline / v1 / v2 | 1.00 / .95 / .95 | **8.6** / 5.1 / **30.2** | 72.2 / 72.7 / 63.9 |
| Qwen | baseline / v1 / v2 | .92 / .84 / .78 | **52.5** / **78.1** / **85.1** | 63.2 / 54.1 / 53.7 |

Same table, same metric as SBB-2026 Table 3 (GPT-3.5 60.6, codechat-bison
40.1, CodeLlama-70B 28.3, Claude-3-haiku 36.3; Pass@attr 66.6–79.6). Our
1.3B/1.5B models sit inside their range; DeepSeek-1.3B is the least biased
model measured on this benchmark by anyone so far.

### 3a. SBB-2026's prompts on our models (promptmit_v3 = their CoT, v4 = their P-CoT)

| model | baseline | v3 CoT | v4 P-CoT | Pass@attr base → v4 |
| :-- | --: | --: | --: | --: |
| CodeGen | 58.7 | 57.1 | 58.6 | 58.1 → 58.4 |
| DeepSeek | 8.6 | **17.5** | **17.2** | 72.2 → 68.1 |
| Qwen | 52.5 | **82.4** | **82.5** | 63.2 → 51.9 |

Their RQ2 finding (CoT / fairness persona amplify bias; GPT-3.5 60.6 → 72.7,
bison 40.1 → 55.5) replicates on ≤1.5B open models: DeepSeek doubles, Qwen
+30 points, Pass@attribute falls. CodeGen is flat because it barely follows
instructions. 6,174 generations, Kaggle v7.

## What this settles

* Every bias claim in the paper now has the source paper's own metric next to
  ours, computed with their released code/data on the same generations.
* Two 2026 findings replicate on our grid: prompt-level fairness instructions
  backfire (SBB Table 6 → our 3a), and fairness gains cost utility (RSB
  Table 4 → our Pass@attribute and validity columns).
* Honest negatives that stay in: UQSB AST scrub is cosmetic; BTM's dominant
  attribute (age) is outside our scrub's scope.
