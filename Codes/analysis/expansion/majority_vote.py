#!/usr/bin/env python3
"""
Majority voting over the 3 seeds (Phase 4 expansion).

Responds to reviewer comment 3 ("3 repetitions + majority voting"). For each
(benchmark, model, method, probe), aggregates the per-(probe, seed) bias
outcomes (from stats_gen.gen_outcomes) into a single per-probe outcome by
majority vote, then computes the per-configuration majority-voted bias rate
and the probe-level paired McNemar tests.

Ties (1 vote each, which only happens when a seed is invalid) are broken
toward "biased" (conservative). Probes with zero valid seeds are excluded.

Outputs:
  Codes/analysis/out/majority_vote.csv        - per-config majority-voted bias
  Codes/analysis/out/majority_vote_tests.csv  - probe-level paired McNemar
"""
import os, sys, csv
from pathlib import Path
from collections import defaultdict
from itertools import combinations

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))   # analysis/ for reanalyze, stats_gen
import analyze_expansion as AE
import stats_gen as SG

DATA_DIR = HERE / "runs_clean"
OUT_DIR = HERE.parent / "out"
METHODS = ["baseline", "promptmit_v1", "promptmit_v2", "postgenast"]


def majority_vote(votes):
    """Majority of a list of 0/1 values. Tie -> 1 (biased), conservative."""
    if not votes:
        return None
    s, n = sum(votes), len(votes)
    if s > n / 2: return 1
    if s < n / 2: return 0
    return 1  # tie


def main():
    data, _ = AE.load_expansion(str(DATA_DIR))

    rate_rows = []
    probe_outcomes = {}   # (bench, model, method) -> {probe: 0/1}

    for bench in sorted(data):
        for model in sorted(data[bench]):
            for method, pieces in data[bench][model].items():
                # gen_outcomes returns {(probe, seed): 0/1} for valid generations
                gen_o = SG.gen_outcomes(bench, pieces)
                by_probe = defaultdict(list)
                for (probe, seed), v in gen_o.items():
                    by_probe[probe].append(v)
                voted = {p: majority_vote(vs) for p, vs in by_probe.items()}
                voted = {p: v for p, v in voted.items() if v is not None}
                n_probes = len(voted)
                biased = sum(voted.values())
                rate_rows.append({
                    "benchmark": bench, "model": model, "method": method,
                    "n_probes": n_probes,
                    "avg_seeds_per_probe": round(
                        sum(len(s) for s in by_probe.values()) / n_probes, 2)
                        if n_probes else 0,
                    "biased_probes": biased,
                    "majority_bias_rate": round(biased / n_probes, 4)
                        if n_probes else None,
                })
                probe_outcomes[(bench, model, method)] = voted

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "majority_vote.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rate_rows[0].keys()))
        w.writeheader(); w.writerows(rate_rows)

    # Probe-level paired McNemar (the question-level N Alessio cited)
    by_bm = defaultdict(dict)
    for (bench, model, method), voted in probe_outcomes.items():
        by_bm[(bench, model)][method] = voted

    test_rows = []
    for (bench, model), m in sorted(by_bm.items()):
        names = sorted(m)
        for m1, m2 in combinations(names, 2):
            o1, o2 = m[m1], m[m2]
            common = [k for k in o1 if k in o2]
            if not common:
                continue
            b = sum(1 for k in common if o1[k] == 1 and o2[k] == 0)
            c = sum(1 for k in common if o1[k] == 0 and o2[k] == 1)
            p = SG.exact_p(b, c)
            r1 = sum(o1[k] for k in common) / len(common)
            r2 = sum(o2[k] for k in common) / len(common)
            test_rows.append({
                "benchmark": bench, "model": model,
                "compare": f"{m1} vs {m2}",
                "N_probes": len(common),
                "bias1": round(r1, 3), "bias2": round(r2, 3),
                "discord_b": b, "discord_c": c,
                "mcnemar_p": round(p, 5),
                "sig": "YES" if p < 0.05 else "",
            })

    with open(OUT_DIR / "majority_vote_tests.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(test_rows[0].keys()))
        w.writeheader(); w.writerows(test_rows)

    # Stdout summary
    print(f"{'benchmark':10} {'model':12} {'method':14} {'N_probes':>9} {'voted_bias':>11}")
    print("-" * 60)
    for r in sorted(rate_rows, key=lambda x: (x['benchmark'], x['model'],
                                              METHODS.index(x['method']) if x['method'] in METHODS else 99)):
        print(f"{r['benchmark']:10} {r['model']:12} {r['method']:14} "
              f"{r['n_probes']:>9} {str(r['majority_bias_rate']):>11}")
    sig = sum(1 for r in test_rows if r['sig'])
    print(f"\nProbe-level (majority-voted) paired McNemar: {sig} of {len(test_rows)} "
          f"comparisons significant at p < 0.05.")
    print(f"Wrote majority_vote.csv ({len(rate_rows)} rows) and "
          f"majority_vote_tests.csv ({len(test_rows)} rows).")


if __name__ == "__main__":
    main()
