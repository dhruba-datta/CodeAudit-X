# Adopting the source papers' own metrics — status

Ferrari, 9 Sep: *"same metrics, if they are in the literature they should be
adopted."* This records what each source paper actually measures, what we could
reproduce, and what it shows on the Phase 5 data.

## What the three artifacts actually contain

| Benchmark | Their metric | Their scoring code | Status |
| :-- | :-- | :-- | :-- |
| **BTM-2025** | Metamorphic *execution*: perturb a protected parameter, hold the rest, call the function twice; output differs → biased. BI@5 / BD@5 / BE@5 per attribute, % of prompts. Plus a substring "CBS". | `fast_test_case_inference.py`, `report_biask.py` in `huangd1999/CBS` | **Re-implemented and run.** `metrics_btm_authors.py` |
| **UQSB-2023** | Trained classifier over generated code; CBS = % flagged. | `theNamek/Code-Bias`. **The released checkpoint is an LSTM, not the paper's BERT.** No BERT checkpoint exists anywhere. No CBS/UFS code exists either — formulas are only in the paper. Training data (2,744 labelled snippets) is released. | Checkpoint + data fetched. **Scoring needs torch + the BERT tokenizer → Kaggle.** |
| **BU-2024** | Metamorphic *execution* over the full Cartesian product of demographic values on a dataclass; any output change on a sensitive attribute → biased. CBS, Bias Leaning Score, Pass@attribute computed in notebooks. | `janeeyre912/fairness_testing_code_generation`, `test_suites/utils.py` + 343 pytest suites | Harness understood. **Their prompt is a dataclass with a `(self)` method — not our completion stub.** Faithful use means regenerating BU with their 343 prompts. |

## BTM-2025 under the authors' metric (k = 5, N = 334 prompts)

BI@5 = % of prompts where at least one of five samples is biased on the attribute.

| Model | Method | exec'd | age | education | gender | race | region | occupation | salary |
| :-- | :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| CodeGen-350M | baseline | 470 | 33.2 | 9.9 | 6.3 | 2.7 | 6.6 | 3.3 | 2.7 |
| CodeGen-350M | promptmit_v2 | 490 | 41.6 | 15.6 | 10.2 | 5.4 | 7.5 | 7.5 | 2.1 |
| CodeGen-350M | **postgenast** | 346 | 44.3 | 18.3 | **0.0** | **0.0** | 0.0 | 6.9 | 2.4 |
| DeepSeek-1.3B | baseline | 123 | 5.1 | 5.1 | 2.1 | 0.9 | 1.8 | 1.2 | 0.3 |
| DeepSeek-1.3B | promptmit_v2 | 89 | 5.7 | 3.9 | 0.9 | 0.0 | 2.4 | 0.6 | 0.3 |
| DeepSeek-1.3B | **postgenast** | 100 | 3.0 | 3.6 | **0.0** | **0.0** | 0.0 | 1.2 | 0.3 |
| Qwen-1.5B | baseline | 95 | 7.5 | 3.3 | 1.8 | 0.6 | 3.3 | 2.1 | 1.2 |
| Qwen-1.5B | promptmit_v2 | 234 | 13.5 | 6.6 | 1.8 | 0.0 | 5.7 | 2.4 | 0.3 |
| Qwen-1.5B | **postgenast** | 81 | 6.3 | 3.0 | **0.0** | **0.0** | 0.0 | 2.4 | 1.2 |

BD@5 (all five samples biased) is 0.00 everywhere — stochastic small models never
agree five times. Full table: `BTM_authors_metrics_k5.csv`.

### What it shows

1. **Cross-metric agreement on the central claim.** Under the authors' own
   execution-based metric, AST scrubbing drives *gender* and *race* to exactly
   0.0 on all three models — the same conclusion our CLPUR gave. Two
   independent instruments, one answer.

2. **And an honest boundary on it.** Scrubbing does *not* reduce age /
   education / occupation / salary under their metric, because our scrub
   targets only {gender, race, region}. Their metric counts seven attributes.
   The paper should say the scrub is attribute-scoped and name the scope.

3. **Age dominates**, 5–44% BI@5. The authors report the same pattern on
   GPT-4-class models. Independent replication of their qualitative finding on
   small open models.

4. **The metric was built for instruction-following models.** It only fires
   when the generated function takes protected attributes *as named
   parameters*. CodeGen does that ~29% of the time; DeepSeek and Qwen 5–14%.
   The rest is either prose (unparsed) or falls to the authors' own fallback
   rule (substring `" if <attr> "`). So on small models most of the signal is
   the fallback, not execution — a limitation of *their* metric on *our*
   models, and worth one sentence in Threats to Validity.

5. **Departures from their code, all conservative:** other-parameter
   combinations capped at 12 per value pair (they had no cap; sampling can only
   miss bias, never invent it); each generation sandboxed in a subprocess with
   CPU/memory/time limits; only protected parameters perturbed (identical
   result, less compute).

## A bug this exposed — BTM promptmit_v1 was a no-op

`prompts.py` implemented v1 as `text.replace("Return only Python code.", ...)`.
That phrase exists in the Phase-4 reconstructed prompts and **not** in the
authors' released ones. On the real dataset, v1 rewrote nothing: **333 of 334
Qwen seed-1 generations are byte-identical to baseline.** Every BTM
baseline-vs-v1 comparison in `FULL_expanded_tests.csv` is therefore a
comparison of a condition with itself (which is why they all show p = 1.0).

Fixed: v1 now appends the constraint when the phrase is absent. **BTM
promptmit_v1 must be regenerated** — 334 × 3 models × 5 seeds ≈ 5,010
generations, ~20 min on Kaggle. Until then, treat BTM v1 rows as invalid.

## What needs Kaggle (one notebook, ~1 hour)

1. **Regenerate BTM promptmit_v1** with the fixed prompt.
2. **Regenerate BU-2024 with the authors' 343 prompts** (`dataset/prompts.jsonl`,
   verbatim), so their pytest harness can be applied without adaptation.
   ~9,300 generations.
3. **UQSB classifier scoring:** run the released LSTM checkpoint over every
   UQSB generation → CBS_LSTM. Optionally retrain BERT-base on their 2,744
   labelled snippets per the paper's recipe (lr 1e-5, 5 epochs, ~5 min on a
   T4) → CBS_BERT. Report both alongside our ContextBiasRate.

## Not adopted, with reasons

- **SEB-2023** — Ferrari's reframing makes it a cognitive-bias benchmark; its
  original metrics (keyword-reliance, name-memorisation) are a different
  study. Keep PerturbationBiasRate, describe it as ours.
- **IMSB-2025** — FAST scores apply to editing BERT/GPT-2 weights, not to
  prompting code models. Not transferable. Keep BiasKnowledgeRate, describe
  it as our extension.

## Files

- `metrics_btm_authors.py` — the re-implementation, with every departure
  from their code documented inline
- `BTM_authors_metrics_k5.csv` — 4 methods × 3 models × 7 attributes × 4 metrics
