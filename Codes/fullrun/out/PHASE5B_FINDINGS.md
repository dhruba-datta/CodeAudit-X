# Phase 5b — regeneration, extraction fix, value-aware UQSB (9 Sept 2026)

Supersedes the UQSB, BU-2024 and BTM-v1 numbers in FULL_STUDY_FINDINGS.md.
Kaggle version 4 (116 min, T4x2): 22,851 generations — BTM promptmit_v1
regenerated (3,006), BU-2024A authors' prompts (9,261), UQSB regenerated for
the classifier (10,584). Merged with `merge_regen.py`; study shards backed up
as `*.jsonl.pre-v1fix`.

## 1. BTM promptmit_v1 fix took

Regenerated v1 differs from baseline on 334/334 prompts per model (was 1/334).
Study now has a real v1 arm on BTM. Under our CLPUR: codegen 0.29→0.31,
deepseek 0.19→0.30, qwen 0.23→0.25 — v1 does **not** help on BTM, and on
DeepSeek it is significantly worse than baseline (b=47, c=110). Validity moved
up (0.72/0.47/0.44 → 0.83/0.71/0.58), because the old "v1" was byte-identical
to baseline and the earlier figure was an artefact of that.

## 2. Completion-stub extraction bug also affected UQSB-2023 (and BU-2024)

Liu et al.'s real prompts end with the target signature and the model returns
the body followed by further functions. `clean_code()` took the first `def` it
saw, i.e. a hallucinated neighbour: in the study's UQSB shards the `code` field
was the target function in **0–4 of 1,176 records per model**. BU-2024 outputs
carry trailing extra functions in 10–51 % of records, which inflated its
CodeBiasScore. Phase 4 was not affected (curated prompts had no trailing
signature). Fix in `extract_and_score.completion_code()`: scored code =
signature + body, truncated at the next top-level definition; target function
now recovered in 1,176/1,176.

## 3. UQSB's ContextBiasRate is degenerate under the paper-exact prompts

With the target function scored correctly, "attribute appears in a condition"
is 0.998–1.000 in every cell — the few-shot prompt makes every sensible
completion filter on the parameter. It cannot separate
`== 'white'` (selects a group) from `== 'confident'` (nonsense value).
Liu et al.'s classifier exists for exactly that distinction, and their released
labels split cleanly on the compared value. `uqsb_values.py` implements that
as a deterministic rule (DemographicValueRate: an `if` compares against a
demographic group value). Against their 3,920 labels: acc 0.94, precision
0.97, recall 0.90. This is UQSB's bias metric in the full run from now on.

| model | baseline | v1 | v2 | postgenast |
| :-- | --: | --: | --: | --: |
| codegen350M | 0.206 | 0.224 | 0.247 | 0.206 |
| deepseek1.3b | 0.607 | 0.579 | 0.560 | 0.607 |
| qwen1.5b | 0.497 | 0.529 | 0.559 | 0.497 |

Prompt mitigation raises UQSB bias on CodeGen and Qwen and lowers it slightly
on DeepSeek — the same "unreliable, can backfire" pattern as elsewhere.
**postgenast is identical to baseline**: the UQSB scrub only renames the
attribute (`person[field] == 'white'`), it does not remove the group
selection. The earlier UQSB postgenast PASS cells (0.018 / 0.084) were an
artefact of the wrong function + attribute-name metric. Honest reading: the
AST scrub as implemented for UQSB is cosmetic. A value-aware scrub is a design
change and is not made here.

## 4. Headline numbers after the fix

| | before (FULL_STUDY_FINDINGS) | after |
| :-- | --: | --: |
| McNemar significant (p<0.05) | 49 / 90 | **52 / 90** |
| double-gate PASS cells | 6 / 60 | **1 / 60** (IMSB-2025 / DeepSeek / postgenast: BKR 0.00, V 0.57) |
| UQSB bias metric | ContextBiasRate | DemographicValueRate |

Per-benchmark significant: UQSB 14, BTM 12, BU 11, IMSB 8, SEB 7.

## 5. Authors' metrics status

* BTM (Huang et al.) BI@5/BD@5/BE@5/CBS: rerun on the fixed data,
  `BTM_authors_metrics_k5.csv`. AST scrub still drives gender and race to 0.0
  on all three models; prompt v1/v2 do not.
* UQSB classifier: the Kaggle run scored the wrong function (bug §2). Numbers
  kept as `UQSB_authors_classifier_PRELIM_wrongfunc.csv`, not to be reported.
  Rerun needed on the study's UQSB generations with the fixed extraction.
* BU-2024A: 9,261 generations of the authors' 343 prompts in `runs/BU-2024A/`,
  ready for SBB-2026's harness (CBS / BLS@Range / Pass@attribute).

## 6. Reproducibility of the regeneration

Same seeds, same T4, same vLLM: UQSB raw output byte-identical to the study in
93.2 % (Qwen) and 84.5 % (DeepSeek) of records. CodeGen via the transformers
backend: 0.1 % — batched HF sampling is not reproducible across batch
compositions (`--hf-batch-size` 128 vs 64). Paired comparisons are unaffected
(a probe never splits across runs), but CodeGen absolute rates from different
sessions should not be mixed without saying so.
