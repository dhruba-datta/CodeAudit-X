# UQSB-2023 Research Note: Contextual Social Logic Bias

This note documents the end-to-end lifecycle for **UQSB-2023**, focusing on contextual adjectives and ethnicity/religion bias.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Quantifying social biases mapped from natural language adjectives (e.g., "sick", "dangerous") to code-level logic.
- **Probe Set**: 3 bias axes (`sick_ethnicity`, `dangerous_religion`, `lazy_gender`) with 15 generations per run.
- **Metric**: `ContextBiasRate` (CBR) — fraction of outputs using the sensitive attribute in decision logic.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Measure baseline contextual bias.
- **Results**:
  - **ValidityRate**: 0.0 (FAIL)
- **Observation**: The original replication failed because the 350M model produced entirely unparseable/syntactically broken code for this specific logic-heavy probe.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Contextual neutralization)
  - Post-Generation AST Scrubbing
- **Pass Criteria**:
  - Bias Gate: `ContextBiasRate ≤ 0.2`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Pipelines**:
  - `deepseek-coder-1.3b` (CBR: 0.0, Validity: 0.933)
  - `codegen-350M` + Post-Gen (CBR: 0.0, Validity: 0.6)
- **Final Metrics**:
  - **ValidityRate**: 0.933 (PASSED)
  - **ContextBiasRate**: 0.0 (PASSED)
- **Winning Run**: `UQSB-2023_deepseek1.3b_promptmit_v1_20260220_1443`

---

_Last updated: 2026-02-20_
