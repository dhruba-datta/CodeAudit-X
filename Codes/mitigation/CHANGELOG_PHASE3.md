# Phase 3 - Mitigation Changelog

All notable changes to the Phase 3 Mitigation research will be documented in this file.

## [2026-02-19] - Phase 3 Initialization

- Locked Phase 2 state.
- Created directory structure for Phase 3.
- Initialized `RUN_REGISTRY.csv` and `CHANGELOG_PHASE3.md`.

## [2026-02-19] - Phase 3 Pilot: BTM-2025 Refinement & Re-evaluation

- Executed Pilot Refinement runs: v2 (strict prompt) and v3 (relaxed prompt/robust extraction).
- Performed **Refined Metric Patching**:
  - Classidied attributes into **Protected** (gender, race, region) vs **Allowed** (age, etc.).
  - Introduced `StringEchoRate` to quantify prompt leakage.
- **Key Findings**:
  - **CodeLevelProtectedUsageRate: 0.0** across all mitigation runs (PASSED bias gate).
  - **ValidityRate: 0.4** (FAILED utility gate).
  - identified "String Echoing" as the primary source of previously high bias scores.
- Created refined comparison report: `Codes/mitigation/comparisons/BTM-2025/BTM-2025_codegen350M_refined_comparison.json`.
- **Conclusion**: Success gate NOT MET due to utility loss. Recommended pivot to Post-Generation AST rewriting.
