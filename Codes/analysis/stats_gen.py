#!/usr/bin/env python3
"""
Generation-level paired tests. Sample unit = a single generation, keyed by
(probe, seed) for per-piece benchmarks or (task, seed) metamorphic group for
SEB/BU. This raises N from 3-4 questions to 15-20 generations per config and
lets us pair two techniques on the SAME (probe, seed) and apply McNemar's exact
test (the correct test for paired binary bias outcomes).

NOTE on units (for the paper): question-level N is only 3-4 per benchmark, which
is the true root cause of the 'small numbers'. Generation-level tests are valid
for stochastic decoding but do not substitute for more QUESTIONS; both are
reported, and probe expansion remains the real fix for question-level power.
"""
import os, csv
from collections import defaultdict
from itertools import combinations
import reanalyze as R
try:
    from scipy.stats import binomtest
    def exact_p(b, c):
        n = b + c
        return binomtest(min(b, c), n, 0.5, alternative="two-sided").pvalue if n else 1.0
except Exception:
    from math import comb
    def exact_p(b, c):
        n = b + c
        if n == 0: return 1.0
        k = min(b, c)
        return min(1.0, 2*sum(comb(n, i) for i in range(k+1))/(2**n))

METAMORPHIC = {"SEB-2023", "BU-2024"}

def gen_outcomes(bench, pieces):
    """key -> biased(0/1) for valid generations only."""
    out = {}
    if bench in METAMORPHIC:
        byps = defaultdict(list)
        for p in pieces:
            byps[(p["probe"], p["seed"])].append(p)
        for key, g in byps.items():
            valid = [x for x in g if x["valid"]]
            if len(valid) >= 2:
                out[key] = 1 if len({x["return_type"] for x in valid}) > 1 else 0
    else:
        for p in pieces:
            if p["valid"] and p["biased"] is not None:
                out[(p["probe"], p["seed"])] = 1 if p["biased"] else 0
    return out

def collect():
    data = defaultdict(lambda: defaultdict(dict)); seen = set()
    for bench, model, method, run_dir, ext, kind in R.discover_runs():
        load, _, _ = R.ADAPTERS[bench]
        pieces = load(ext)
        if not pieces: continue
        label = method if kind == "mitigation" else "baseline"
        key = (bench, model, label)
        if key in seen:
            if not (bench == "BTM-2025" and len({p["probe"] for p in pieces}) == 3 and len(pieces) == 15):
                continue
        seen.add(key)
        data[bench][model][label] = gen_outcomes(bench, pieces)
    return data

def main():
    data = collect(); rows = []
    for bench in R.ADAPTERS:
        for model in sorted(data[bench]):
            methods = sorted(data[bench][model])
            for m1, m2 in combinations(methods, 2):
                o1, o2 = data[bench][model][m1], data[bench][model][m2]
                common = [k for k in o1 if k in o2]
                if len(common) < 6:  # still report but flag
                    pass
                b = sum(1 for k in common if o1[k] == 1 and o2[k] == 0)  # m1 biased, m2 not
                c = sum(1 for k in common if o1[k] == 0 and o2[k] == 1)
                if not common: continue
                p = exact_p(b, c)
                r1 = sum(o1[k] for k in common)/len(common)
                r2 = sum(o2[k] for k in common)/len(common)
                rows.append({
                    "benchmark": bench, "model": model, "compare": f"{m1} vs {m2}",
                    "N_gen": len(common),
                    "bias1": round(r1, 3), "bias2": round(r2, 3),
                    "discord_b": b, "discord_c": c,
                    "mcnemar_p": round(p, 5),
                    "sig": "YES" if p < 0.05 else "",
                })
    with open(os.path.join(R.OUTDIR, "pairwise_tests_generation.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("GENERATION-LEVEL PAIRED McNEMAR (sample = generation, paired by probe x seed)")
    print(f"{'benchmark':10} {'model':12} {'comparison':28} {'N':>3} {'b1/b2':>11} {'b,c':>7} {'p':>8} sig")
    print("-"*86)
    for r in sorted(rows, key=lambda x:(x['benchmark'], x['model'])):
        print(f"{r['benchmark']:10} {r['model']:12} {r['compare']:28} {r['N_gen']:>3} "
              f"{r['bias1']:>5}/{r['bias2']:<5}{str(r['discord_b'])+','+str(r['discord_c']):>7} "
              f"{r['mcnemar_p']:>8} {r['sig']}")
    sig = sum(1 for r in rows if r['sig'])
    print(f"\n{sig} of {len(rows)} comparisons significant at p<.05. Wrote pairwise_tests_generation.csv")

if __name__ == "__main__":
    main()
