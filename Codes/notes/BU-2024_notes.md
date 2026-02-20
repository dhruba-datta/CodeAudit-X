# BU-2024 Research Note: Metamorphic Flow Bias

This note documents the end-to-end lifecycle for **BU-2024**, employing the Solar framework for metamorphic testing.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Using metamorphic relations (e.g., swapping names/demographics) to unveil hidden social biases in structural code decisions.
- **Probe Set**: 3 tasks across 4 metamorphic variants with 7 demographic dimensions.
- **Demographic Dimensions**: `race`, `age`, `marital_status`, `education`, `gender`, `religion`, `employment_status`.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Quantify variance in code structure across demographic variants using the Code Bias Score (CBS).
- **Results**:
  - **CodeBiasScore (CBS)**: High variance (0.7+)
- **Observation**: The model's logic for the same functional task differed significantly based on the demographic description in the docstring.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Structural consistency)
  - Post-Generation Logic Scrubbing (Standardization of decision nodes)
- **Pass Criteria**:
  - Bias Gate: `CBS ≤ 0.2`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Pipeline**: `qwen-1.5b-instruct` + Post-Gen Normalization
- **Final Metrics**:
  - **ValidityRate**: 1.0 (PASSED)
  - **CodeBiasScore (CBS)**: 0.0 (PASSED)
- **Winning Run**: `BU-2024_qwen1.5b_postgen_v1_20260220_1411`

---

_Last updated: 2026-02-20_
