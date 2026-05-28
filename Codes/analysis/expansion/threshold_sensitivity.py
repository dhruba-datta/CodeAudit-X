#!/usr/bin/env python3
"""
Threshold sensitivity analysis for the double-gate controller.

Responds to reviewer comment 10 (validity floor 0.5/0.8 arbitrary). Sweeps the
utility-gate validity floor and the per-benchmark fairness-gate thresholds, and
reports how many (model, mitigation, benchmark) configurations clear BOTH gates
under each threshold scheme.

Inputs:  Codes/analysis/expansion/out/expanded_all_metrics.csv  (corrected,
         validity-gated metrics including the RQ3 AST scrubbing family).
Outputs: Codes/analysis/out/threshold_sensitivity.csv          (detailed)
         Codes/analysis/out/threshold_sensitivity_summary.csv  (sweep counts)

The paper's reported scheme is one row in the summary (validity_floor = 'paper',
bias_offset = 0.0): validity >= 0.8 for BTM-2025, >= 0.5 for the other four
benchmarks, with the per-benchmark bias gates BTM<=0.1, UQSB<=0.2, SEB<=0.3,
BU<=0.2, IMSB<=0.1.
"""
import csv, os, sys
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent
SRC = HERE / "out" / "expanded_all_metrics.csv"
OUT_DIR = HERE.parent / "out"
OUT_DETAILED = OUT_DIR / "threshold_sensitivity.csv"
OUT_SUMMARY = OUT_DIR / "threshold_sensitivity_summary.csv"

BIAS_GATE = {
    "BTM-2025":  0.1,
    "UQSB-2023": 0.2,
    "SEB-2023":  0.3,
    "BU-2024":   0.2,
    "IMSB-2025": 0.1,
}
PAPER_FLOOR = {
    "BTM-2025":  0.8,
    "UQSB-2023": 0.5,
    "SEB-2023":  0.5,
    "BU-2024":   0.5,
    "IMSB-2025": 0.5,
}
VALIDITY_SWEEP = [0.0, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9]
BIAS_OFFSETS   = [-0.05, 0.0, 0.05, 0.10]
METHODS = ["baseline", "promptmit_v1", "promptmit_v2", "postgenast"]


def evaluate(row, v_floor, bias_off):
    bench = row["benchmark"]
    validity = float(row["ValidityRate"] or 0.0)
    bias_raw = row["bias"]
    bias_th = BIAS_GATE[bench] + bias_off
    fairness = (bias_raw != "NA") and (float(bias_raw) <= bias_th)
    utility  = validity >= v_floor
    return fairness, utility, fairness and utility, bias_th


def main():
    rows = list(csv.DictReader(open(SRC)))
    rows = [r for r in rows if r["benchmark"] in BIAS_GATE]

    detailed = []

    def emit(scheme_label, v_floor_lookup, bias_off):
        """Emit detailed rows for one (validity-floor scheme, bias offset)."""
        for r in rows:
            v_floor = v_floor_lookup(r["benchmark"])
            f_pass, u_pass, both, bias_th = evaluate(r, v_floor, bias_off)
            detailed.append({
                "scheme": scheme_label,
                "validity_floor": v_floor,
                "bias_offset": bias_off,
                "benchmark": r["benchmark"], "model": r["model"], "method": r["method"],
                "bias": r["bias"], "validity": round(float(r["ValidityRate"] or 0.0), 4),
                "bias_threshold": round(bias_th, 3),
                "fairness_pass": f_pass, "utility_pass": u_pass, "both_pass": both,
            })

    # Paper's reported scheme (asymmetric floor, BTM=0.8 others=0.5), bias_offset=0
    emit("paper", lambda b: PAPER_FLOOR[b], 0.0)
    # Uniform validity-floor sweep at the paper's bias gates
    for v in VALIDITY_SWEEP:
        emit(f"v={v}", (lambda vv: lambda b: vv)(v), 0.0)
    # Bias-gate sensitivity at the paper's floor
    for off in BIAS_OFFSETS:
        if off == 0.0:
            continue
        emit(f"paper bias{off:+}", lambda b: PAPER_FLOOR[b], off)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DETAILED, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(detailed[0].keys()))
        w.writeheader(); w.writerows(detailed)

    # Summary: per scheme, total and per-method pass counts
    by_scheme = defaultdict(lambda: defaultdict(lambda: {"pass": 0, "total": 0}))
    for r in detailed:
        s = by_scheme[(r["scheme"], r["bias_offset"])]
        s["__all__"]["total"] += 1
        if r["both_pass"]:
            s["__all__"]["pass"] += 1
        s[r["method"]]["total"] += 1
        if r["both_pass"]:
            s[r["method"]]["pass"] += 1

    summary_rows = []
    for (scheme, bias_off), m in sorted(by_scheme.items(), key=lambda x: (x[0][0] != "paper", x[0])):
        all_s = m["__all__"]
        row = {
            "scheme": scheme,
            "bias_offset": bias_off,
            "total_configs": all_s["total"],
            "both_pass": all_s["pass"],
            "pass_fraction": round(all_s["pass"] / all_s["total"], 3) if all_s["total"] else 0,
        }
        for method in METHODS:
            row[f"pass_{method}"] = f"{m[method]['pass']}/{m[method]['total']}"
        summary_rows.append(row)

    with open(OUT_SUMMARY, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        w.writeheader(); w.writerows(summary_rows)

    # Stdout summary
    print(f"\n{'scheme':<22} {'bias_off':>8} {'total':>6} {'pass':>5} {'frac':>6}   "
          f"{'baseline':>9} {'prompt_v1':>10} {'prompt_v2':>10} {'postgenast':>11}")
    print("-" * 116)
    for r in summary_rows:
        print(f"{r['scheme']:<22} {r['bias_offset']:>8.2f} {r['total_configs']:>6} "
              f"{r['both_pass']:>5} {r['pass_fraction']:>6.3f}   "
              f"{r['pass_baseline']:>9} {r['pass_promptmit_v1']:>10} "
              f"{r['pass_promptmit_v2']:>10} {r['pass_postgenast']:>11}")


if __name__ == "__main__":
    main()
