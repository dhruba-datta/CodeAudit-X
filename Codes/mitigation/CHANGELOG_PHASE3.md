# Phase 3 - Mitigation Changelog

All notable changes to the Phase 3 Mitigation research will be documented in this file.

## [2026-02-19] - Phase 3 Initialization

- Locked Phase 2 state.
- Created directory structure for Phase 3.
- Initialized `RUN_REGISTRY.csv` and `CHANGELOG_PHASE3.md`.

## [2026-02-19] - Phase 3.1: Post-Generation Mitigation (BTM-2025)

- Implemented AST-based identifier/subscript scrubbing in `postgen_btm_ast_v1.py`.
- Source Run: `BTM-2025_codegen350M_promptmit_v2_20260219_190744`.
- **Key Findings**:
  - **CodeLevelProtectedUsageRate: 0.0** (PASSED bias gate).
  - **ValidityRate: 0.4** (FAILED utility gate).
  - Post-gen scrubbing failed to recover validity because source files were mostly empty or syntactically broken.
- Created comparison report: `Codes/mitigation/comparisons/BTM-2025/BTM-2025_codegen350M_postgen_v1_vs_baseline_v2.json`.
- **Final Recommendation**: Prompt-level and post-gen strategies on `codegen-350M-mono` are blocked by the model's low instruction-following capability. **Pivot to a more capable model (e.g., 3B+ parameters)** for the next pilot.

## [2026-02-19] - Phase 3.2: Model Pivot Pilot (BTM-2025)

- **Model**: `Qwen/Qwen2.5-Coder-1.5B-Instruct` (Pivoted from StarCoder2-3B due to 16GB RAM limit).
- **Setup**: Used MPS (Metal) acceleration on Mac.
- **Key Findings**:
  - **CodeLevelProtectedUsageRate: 0.0** (PASSED bias gate).
  - **ValidityRate: 0.6** (IMPROVED but FAILED 0.8 gate).
  - **StringEchoRate: 0.06** (Leakage significantly reduced).
  - Failure mode: **Model laziness** (returning `# Your code here` placeholders).
- Created comparison report: `Codes/mitigation/comparisons/BTM-2025/BTM-2025_qwen1.5b_vs_baseline.json`.

## [2026-02-19] - Phase 3.2.1: Qwen v2 Refinement (Anti-Placeholder)

- **Model**: `Qwen/Qwen2.5-Coder-1.5B-Instruct`
- **Result**: `ValidityRate: 0.4`, `CodeLevelProtectedUsageRate: 0.0`.
- **Finding**: Regression in validity (from 0.6 down to 0.4). Strict anti-placeholder prompts did not resolve model laziness.
- **Decision**: success gate (0.8) FAILED. Proceeding with Post-Generation AST pass on v2 as a last attempt.

## [2026-02-19] - Phase 3.3: DeepSeek-Coder-1.3B Pivot

- **Model**: `deepseek-ai/deepseek-coder-1.3b-instruct`
- **Result**: `ValidityRate: 0.733`, `CodeLevelProtectedUsageRate: 0.20`, `StringEchoRate: 0.267`.
- **Finding**: Highest validity of any model (11/15 valid). Bias gate failed due to AI_03 prompt causing model to read protected attrs. Post-gen AST scrub recommended.
- **Next**: Run post-gen scrub to neutralize bias and re-evaluate.

## [2026-02-19] - Phase 3.3: DeepSeek Post-Gen Scrub + Cleanup

- **Post-Gen Result**: `ValidityRate: 0.733`, `CodeLevelProtectedUsageRate: 0.0`, `StringEchoRate: 0.267`.
- **Gate**: Bias PASSED (0.0). Validity NEAR MISS (0.733 < 0.8).
- **Cleanup**: Archived 10 unregistered intermediate runs to `runs/_archive/`.
- **Updated**: `BTM-2025_pilot_final_status.json`, created `BTM-2025_deepseek1.3b_postgen_v1_vs_all.json`.
- **Next**: DeepSeek v2 prompt refinement targeting AI_01 to push validity past 0.8.

## [2026-02-19] - Phase 3.3.1: DeepSeek v2 Prompt Refinement — GATE PASSED 🎉

- **Model**: `deepseek-ai/deepseek-coder-1.3b-instruct` (v2 prompt)
- **Prompt Change**: Refined AI_01 to require feature-based scoring with minimum 3 if-elif branches. Kept AI_02/AI_03 unchanged.
- **Prompt Result**: `ValidityRate: 0.80`, `CodeLevelProtectedUsageRate: 0.20`, `StringEchoRate: 0.133`.
- **Post-Gen Result**: `ValidityRate: 0.867`, `CodeLevelProtectedUsageRate: 0.0`, `StringEchoRate: 0.133`.
- **Gate**: Bias PASSED (0.0 ≤ 0.1). Validity PASSED (0.867 ≥ 0.8).
- **Decision**: BTM-2025 pilot FROZEN. Pipeline ready for cross-paper scaling to UQSB-2023 and FC-2025.

## [2026-02-20] - FC-2025: Task-Based Refactor & Full Execution

- **Refactored** FC-2025 pipeline into two explicit tasks: `function_implementation` and `test_case_generation`.
- **Metrics**: Swapped generic bias metrics for paper-specific `RefusalRate`, `PreferenceEntropy`, and `FairScore` (R + E − R×E).
- **Configs**: Created per-task directories under `configs/FC-2025/` with prompt and postgen configs per model.
- **Scripts**: Built `fc_metrics.py` (metric engine), `run_fc_pilot.py` (runner), `postgen_fc_ast.py` (scrubber), `build_comparisons.py` (comparison builder).
- **Executed**: v1 and v2 prompt mitigations + postgen AST scrub across all 3 models (codegen350M, qwen1.5b, deepseek1.3b) for both tasks.
- **Baseline**: Retroactively extracted FC metrics from the codegen350M baseline run.

## [2026-02-20] - FC-2025: Edge Case Fix & Cleanup

- **Fixed `fc_metrics.py`**: FairScore now returns `"NA"` (instead of 1.0) when ValidityRate=0.0 — prevents over-crediting failed runs.
- **Patched**: 6 existing metrics files corrected in-place.
- **Archived & Deleted**: 19 old/superseded runs removed (pre-refactor and duplicate retries). No `_archive` folder kept.
- **Legacy Cleanup**: Removed 9 obsolete comparison files (`*_vs_baseline`, `*_vs_v1`, `*_vs_prompt_best`).
- **Task-Separated Reporting**: Rebuilt all comparisons with per-task verdicts in the final status JSON.

## [2026-02-20] - FC-2025: GATE PASSED ✅

- **Overall Verdict**: PASS
- **Function Implementation**: Qwen-1.5B achieved FairScore=1.0, ValidityRate=1.0 (PASS). DeepSeek-1.3B returned NA (zero valid outputs).
- **Test Case Generation**: CodeGen-350M v2 achieved FairScore=1.0, ValidityRate=0.5 (PASS). Qwen produced valid tests but with low RefusalRate.
- **DeepSeek-1.3B**: FAIL — best real FairScore=0.667 with 0.3 validity (below 0.7 threshold after edge-case correction).
- **Decision**: FC-2025 pilot FROZEN. 18 canonical runs preserved. Next paper: UQSB-2023.
