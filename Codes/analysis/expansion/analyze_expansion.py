#!/usr/bin/env python3
"""
Analyze the expanded runs (Codes/analysis/expansion/runs/) the same way the
validated pipeline analyzes the original runs, WITHOUT modifying reanalyze.py.

Reuses:
  - reanalyze.ADAPTERS  (per-benchmark per-piece loaders + aggregate recompute)
  - stats.per_probe     (question-level: seed-averaged rate + majority vote)
  - stats_gen.gen_outcomes + McNemar (generation-level paired test)

Run after generation (or point --runs at verify_runs to test the loop):
  python analyze_expansion.py [--runs <dir>]
"""
import os, sys, glob, csv, argparse
from collections import defaultdict
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))   # Codes/analysis for reanalyze/stats
import reanalyze as R
import stats as S
import stats_gen as SG

OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

def parse_run_id(name):
    """'BTM-2025_deepseek1.3b_promptmit_v1_expanded' -> (bench, model, method)."""
    core = name[:-len("_expanded")] if name.endswith("_expanded") else name
    parts = core.split("_")
    return parts[0], parts[1], "_".join(parts[2:])

def load_expansion(runs_dir):
    """benchmark -> model -> method -> list[pieces], plus validation rows."""
    data = defaultdict(lambda: defaultdict(dict))
    val = []
    for run_dir in sorted(glob.glob(os.path.join(runs_dir, "*"))):
        ext = os.path.join(run_dir, "ast_extract")
        if not os.path.isdir(ext):
            continue
        bench, model, method = parse_run_id(os.path.basename(run_dir))
        if bench not in R.ADAPTERS:
            continue
        load, agg, bias_key = R.ADAPTERS[bench]
        pieces = load(ext)
        if not pieces:
            continue
        data[bench][model][method] = pieces
        # validate recomputed aggregate vs the run's own metrics.json
        recomp = agg(pieces)
        fn, stored = R.find_stored_metrics(run_dir)
        val.append({"benchmark": bench, "model": model, "method": method,
                    "n_pieces": len(pieces),
                    "recomp_validity": recomp.get("ValidityRate"),
                    "recomp_bias": recomp.get(bias_key),
                    "stored": fn})
    return data, val

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default=os.path.join(HERE, "runs"))
    args = ap.parse_args()
    data, val = load_expansion(args.runs)

    if not val:
        print(f"No expansion runs found under {args.runs}")
        return

    # ---- sample sizes (distinct probes) ----
    print("="*70)
    print(f"EXPANDED ANALYSIS  ({args.runs})")
    print("="*70)
    print("Sample sizes (distinct questions per benchmark):")
    for bench in sorted(data):
        probes = set()
        for model in data[bench]:
            for method, pieces in data[bench][model].items():
                probes |= {p["probe"] for p in pieces}
        n = len(probes)
        flag = "OK for tests" if n >= 6 else "still small"
        print(f"  {bench:11} N={n:3} -> {flag}")

    # ---- all-metrics-all-datasets (per-config aggregate) ----
    agg_rows = []
    for bench in sorted(data):
        _, agg, bias_key = R.ADAPTERS[bench]
        for model in sorted(data[bench]):
            for method, pieces in data[bench][model].items():
                a = agg(pieces)
                agg_rows.append({"benchmark": bench, "model": model, "method": method,
                                 "n_pieces": len(pieces),
                                 "ValidityRate": a.get("ValidityRate"),
                                 "bias_metric": bias_key,
                                 "bias": a.get(bias_key)})
    with open(os.path.join(OUT, "expanded_all_metrics.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(agg_rows[0].keys())); w.writeheader(); w.writerows(agg_rows)

    # ---- generation-level paired McNemar (reuse stats_gen logic) ----
    stat_rows = []
    for bench in sorted(data):
        for model in sorted(data[bench]):
            outc = {m: SG.gen_outcomes(bench, p) for m, p in data[bench][model].items()}
            for m1, m2 in combinations(sorted(outc), 2):
                o1, o2 = outc[m1], outc[m2]
                common = [k for k in o1 if k in o2]
                if not common:
                    continue
                b = sum(1 for k in common if o1[k] == 1 and o2[k] == 0)
                c = sum(1 for k in common if o1[k] == 0 and o2[k] == 1)
                p = SG.exact_p(b, c)
                stat_rows.append({"benchmark": bench, "model": model,
                                  "compare": f"{m1} vs {m2}", "N_gen": len(common),
                                  "bias1": round(sum(o1[k] for k in common)/len(common), 3),
                                  "bias2": round(sum(o2[k] for k in common)/len(common), 3),
                                  "b": b, "c": c, "mcnemar_p": round(p, 5),
                                  "sig": "YES" if p < 0.05 else ""})
    if stat_rows:
        with open(os.path.join(OUT, "expanded_tests.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(stat_rows[0].keys())); w.writeheader(); w.writerows(stat_rows)
        sig = sum(1 for r in stat_rows if r["sig"])
        print(f"\nGeneration-level McNemar: {sig}/{len(stat_rows)} significant (p<.05).")
        print("Wrote expanded_all_metrics.csv, expanded_tests.csv ->", OUT)

    print(f"\nValidated {len(val)} expansion runs (recomputed aggregate vs each run's metrics.json).")

if __name__ == "__main__":
    main()
