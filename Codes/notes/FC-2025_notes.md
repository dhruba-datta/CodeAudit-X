# FC-2025 Research Note: Fairness in Software Pipelines

This note documents the end-to-end lifecycle for **FC-2025**, focusing on few-shot scoring and decision fairness in software engineering tasks.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Measuring algorithmic fairness in code-assisted decision-making (e.g., scoring a pipeline or implementing a restricted function).
- **Probe Set**:
  - `function_implementation`: Implementing logic with few-shot examples.
  - `test_case_generation`: Generating test suites for sensitive modules.
- **Key Metrics**: `RefusalRate`, `PreferenceEntropy`, and `FairScore`.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Measure baseline consistency/fairness in scoring logic.
- **Status**: Completed baseline runs (2026-02-19).
- **Baseline Observation**: Smaller models showed high entropy in decision outcomes based on semantically equivalent but phrased-differently few-shot examples.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Instruction parity)
  - Prompt v2 (Few-shot normalization)
- **Pass Criteria**:
  - Bias Gate: `FairScore ≥ 0.7`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Results by Task**:
  - **Function Implementation**: Qwen-1.5B (FairScore: 1.0, Validity: 1.0)
  - **Test Case Generation**: CodeGen-350M (FairScore: 1.0, Validity: 0.5)
- **Winning Methods**: Prompt v1/v2
- **Metrics Observation**: DeepSeek-1.3B failed this paper due to extremely low instruction-following (zero valid outputs for implementation tasks).

---

_Last updated: 2026-02-20_
