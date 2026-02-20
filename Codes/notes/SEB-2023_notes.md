# SEB-2023 Research Note: Stability and Prompt Perturbations

This note documents the end-to-end lifecycle for **SEB-2023**, investigating structural instability across prompt variants.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Stability auditing — measuring whether an LLM produces structurally different code for semantically identical prompts.
- **Probe Set**: 3 task groups with 4 perturbation variants each (base, short, formal, implied).
- **Metric**: `PerturbationBiasRate` (PBR) — variance in structural hashes/logic across perturbations.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Establish the baseline instability.
- **Results**:
  - **PBR**: 0.55 (Moderate instability)
- **Observation**: The baseline model was highly sensitive to phrasing, producing different algorithm logic for the same simple functional request.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Consistency preamble)
  - Prompt v2 (Implicit logic stabilization)
- **Pass Criteria**:
  - Bias Gate: `PerturbationBiasRate ≤ 0.3`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Pipeline**: `qwen-1.5b-instruct` + Prompt v1
- **Final Metrics**:
  - **ValidityRate**: 0.55 (PASSED)
  - **PerturbationBiasRate**: 0.23 (PASSED)
- **Winning Run**: `SEB-2023_qwen1.5b_promptmit_v1_20260220_1412`

---

_Last updated: 2026-02-20_
