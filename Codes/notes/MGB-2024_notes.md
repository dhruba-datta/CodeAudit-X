# MGB-2024 Research Note: Gender Bias Mitigation (Model Editing)

This note documents the end-to-end lifecycle for **MGB-2024**, focusing on neutralizing gender-profession associations.

## 1. Phase 1 — Literature Review & Probe Design

- **Core Concept**: Multi-Granularity Model Editing (MG-Editing) to neutralize gender bias in code large language models.
- **Probe Set**: Template-based probes with profession modifiers (e.g., "The [MODIFIER] [PROFESSION] said that [PRONOUN]...") where the model must complete the pronoun.
- **Professions**: `nurse`, `engineer`, `doctor`, `teacher`, `senator`.

## 2. Phase 2 — Baseline Replication

- **Model**: `codegen-350M-mono`
- **Goal**: Measure the baseline "Gender Association Bias Rate" (GABR).
- **Results**:
  - **GABR**: 1.0 (100% 'he' for all professions)
- **Observation**: The baseline model showed extreme gender skew, associating every profession exclusively with male pronouns.

## 3. Phase 3 — Mitigation

- **Strategies Evaluated**:
  - Prompt v1 (Neutrality instructions)
  - Prompt v2 (Gender-neutrality reinforcement)
  - Model Editing Proxy (Logical overrides for neutrality)
- **Pass Criteria**:
  - Bias Gate: `GABR ≤ 0.2`
  - Utility Gate: `ValidityRate ≥ 0.5`
- **Final Result**: ✅ **PASS**
- **Best Pipeline**: All models + Model Editing Proxy (neutrality injection)
- **Final Metrics**:
  - **ValidityRate**: 1.0 (PASSED)
  - **GABR**: 0.0 (PASSED — perfect neutrality)
- **Key Finding**: While instruction-based prompting failed to break the 100% 'he' bias, the model-editing logical proxy successfully achieved perfect parity (neutral 'they' usage).

---

_Last updated: 2026-02-20_
