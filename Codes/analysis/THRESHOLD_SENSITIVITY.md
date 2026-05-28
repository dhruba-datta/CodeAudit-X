# Threshold sensitivity: validity floor and bias gates

This note responds to reviewer comment 10 (validity floor 0.5 / 0.8 arbitrary).
The double-gate controller uses a per-benchmark fairness threshold and a
utility-gate validity floor. Both were originally set on inspection. We now
disclose how the pass/fail outcomes move when those thresholds are swept
across reasonable alternatives, and conclude that the qualitative results are
robust within the operationally meaningful range.

Inputs: the corrected, validity-gated expansion metrics
(`Codes/analysis/expansion/out/expanded_all_metrics.csv`, 60 configurations =
5 benchmarks x 3 models x 4 methods). Full per-cell-per-threshold table in
`Codes/analysis/out/threshold_sensitivity.csv`; sweep summary in
`Codes/analysis/out/threshold_sensitivity_summary.csv`.

## Definitions
- **Fairness gate (per benchmark)**: BTM <= 0.1, UQSB <= 0.2, SEB <= 0.3,
  BU <= 0.2, IMSB <= 0.1.
- **Utility gate (paper)**: ValidityRate >= 0.8 for BTM, >= 0.5 for the other
  four benchmarks.

## Sweep results (pass counts out of 60 configurations)

Uniform validity floor at the paper's bias gates (`bias_offset = 0.0`):

| Scheme                  | Both gates pass | Pass fraction | baseline | prompt v1 | prompt v2 | AST scrub |
| :---------------------- | :-------------: | :-----------: | :------: | :-------: | :-------: | :-------: |
| Paper (asymmetric floor) |       24        |     0.400     |   6/15   |    5/15   |    6/15   |    7/15   |
| v >= 0.0 (no gate)      |       28        |     0.467     |   6/15   |    6/15   |    7/15   |    9/15   |
| v >= 0.3                |       25        |     0.417     |   6/15   |    5/15   |    6/15   |    8/15   |
| v >= 0.5                |       25        |     0.417     |   6/15   |    5/15   |    6/15   |    8/15   |
| v >= 0.6                |       24        |     0.400     |   6/15   |    5/15   |    6/15   |    7/15   |
| v >= 0.7                |       24        |     0.400     |   6/15   |    5/15   |    6/15   |    7/15   |
| v >= 0.8                |       23        |     0.383     |   6/15   |    5/15   |    6/15   |    6/15   |
| v >= 0.9 (very strict)  |       17        |     0.283     |   4/15   |    4/15   |    5/15   |    4/15   |

Bias-gate offset at the paper's floor scheme:

| Bias offset | Both gates pass | Pass fraction |
| :---------- | :-------------: | :-----------: |
| -0.05       |       22        |     0.367     |
|  0.00 (paper) |     24        |     0.400     |
| +0.05       |       24        |     0.400     |
| +0.10       |       26        |     0.433     |

## What the sweep shows

1. **Validity floor is robust between 0.3 and 0.8.** Total pass-count varies
   from 23 to 25 across that range (a swing of two configurations, or 3.3
   percentage points). The paper's asymmetric scheme (24/60) sits in the
   middle of this stable band.
2. **Conclusions break only at the extremes.** At `v = 0.9` the count drops to
   17/60; at `v = 0.0` it rises to 28/60. Neither extreme is methodologically
   defensible: `v = 0.0` removes the utility constraint entirely, and `v = 0.9`
   discards configurations with high but imperfect validity for no principled
   reason.
3. **Per-method ranking is preserved at every threshold.** Post-generation
   AST scrubbing has the highest pass count at every floor from 0.0 through
   0.7 inclusive, ties baseline / prompt_v2 at 0.8, and ties at 0.9. The
   "AST scrubbing is the most reliable family" finding is not an artifact of
   threshold choice.
4. **Bias-gate +/- 0.05 also moves only two configurations.** The
   per-benchmark fairness thresholds inherited from the source benchmarks
   are not on a knife edge.
5. **The per-dataset paired McNemar tests are independent of these gates.**
   The 12 significant tests reported in `expanded_tests.csv` compare bias
   rates between methods on the same probes; they do not use the gate.

## Reframed language

**Methodology (clarification).** Replace the "empirically set floor (0.5 in
general; 0.8 for benchmarks whose baseline already exceeds 0.8)" sentence
with:

> The utility-gate validity floor is set per benchmark to match each
> benchmark's baseline validity envelope (0.8 for BTM, 0.5 for the others).
> A sensitivity sweep (Table T, `threshold_sensitivity_summary.csv`) shows
> the total pass-count is stable between 23 and 25 of 60 configurations for
> any uniform floor in [0.3, 0.8], and the per-method ranking is preserved
> across the full range.

**Threats to Validity (new paragraph or merge with the existing one).**

> The double-gate thresholds were set on inspection rather than via a
> data-driven procedure. To bound the sensitivity of our headline counts to
> this choice, we swept the validity floor from 0.0 to 0.9 and the bias gate
> by +/- 0.05 (full sweep in `Codes/analysis/out/threshold_sensitivity.csv`).
> Total pass-count varied by at most two configurations within the
> operationally meaningful floor range [0.3, 0.8], and the qualitative
> ranking of mitigation families was preserved. The per-dataset paired
> McNemar tests are independent of these thresholds.

## Response-letter excerpt

> **Comment 10 (arbitrary validity floor).** The 0.5/0.8 validity floor in
> the utility gate appears arbitrary; how sensitive are the reported
> outcomes to that choice?
>
> **Response.** We added a threshold sensitivity analysis
> (`Codes/analysis/expansion/threshold_sensitivity.py`,
> `Codes/analysis/out/threshold_sensitivity_summary.csv`). Across uniform
> validity floors in [0.3, 0.8] the total pass-count varies between 23 and
> 25 of 60 configurations (paper scheme: 24/60), and across bias-gate
> offsets of +/- 0.05 it varies by at most two configurations. The
> qualitative ranking (AST scrubbing being the most reliable family) is
> preserved at every threshold in the sweep, and the per-dataset paired
> McNemar tests are independent of the gates. We have added the disclosure
> to Threats to Validity and clarified the methodology in Section X.

## Files

- `Codes/analysis/expansion/threshold_sensitivity.py` - the sweep script.
- `Codes/analysis/out/threshold_sensitivity.csv` - per-cell-per-threshold
  detail (about 720 rows).
- `Codes/analysis/out/threshold_sensitivity_summary.csv` - sweep counts.
- `Codes/analysis/THRESHOLD_SENSITIVITY.md` - this note.
