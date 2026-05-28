#!/usr/bin/env python3
"""
Per-model double-gate PASS breakdown.

Responds to reviewer comment 16 (PASS labels are generous: per-paper PASS
typically means at least one of three models passed). Reads the threshold
sensitivity detailed table for the paper's gate scheme and aggregates by
(model, mitigation family) so the per-model story is visible.

Output: Codes/analysis/out/per_model_pass.csv
"""
import csv
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "out" / "threshold_sensitivity.csv"
OUT = HERE.parent / "out" / "per_model_pass.csv"

FAMILY = {
    "baseline":     "Baseline",
    "promptmit_v1": "Prompt",
    "promptmit_v2": "Prompt",
    "postgenast":   "AST",
}
MODELS = ["codegen350M", "deepseek1.3b", "qwen1.5b"]
FAMILIES = ["Baseline", "Prompt", "AST"]


def main():
    rows = list(csv.DictReader(open(SRC)))
    paper = [r for r in rows if r["scheme"] == "paper" and r["bias_offset"] == "0.0"]

    agg = defaultdict(lambda: defaultdict(lambda:
            {"pass": 0, "partial": 0, "fail": 0, "total": 0}))
    for r in paper:
        fam = FAMILY.get(r["method"])
        if not fam:
            continue
        a = agg[r["model"]][fam]
        a["total"] += 1
        fp = (r["fairness_pass"] == "True")
        up = (r["utility_pass"]  == "True")
        if fp and up:        a["pass"] += 1
        elif fp and not up:  a["partial"] += 1
        else:                a["fail"] += 1

    out = []
    for m in MODELS:
        for fam in FAMILIES:
            a = agg[m][fam]
            out.append({
                "model": m, "family": fam,
                "pass": a["pass"], "partial": a["partial"], "fail": a["fail"],
                "total": a["total"],
                "pass_fraction": round(a["pass"] / a["total"], 3) if a["total"] else 0,
            })

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader(); w.writerows(out)

    print(f"{'model':14} {'family':10} {'pass':>4} {'partial':>7} {'fail':>4} {'total':>5}")
    print("-" * 52)
    for r in out:
        print(f"{r['model']:14} {r['family']:10} {r['pass']:>4} "
              f"{r['partial']:>7} {r['fail']:>4} {r['total']:>5}")
    print(f"\nWrote {OUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
