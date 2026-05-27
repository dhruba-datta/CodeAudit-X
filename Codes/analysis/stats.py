#!/usr/bin/env python3
"""
CodeAudit-X re-analysis stage 2: per-probe metrics, sample sizes, and
per-dataset statistical tests. Reuses the validated loaders from reanalyze.py.

Unit of analysis (per Alessio): a (model, technique, probe) triple. The 5 seeds
are repetitions, collapsed by (a) averaging -> per-probe rate, and (b) majority
vote -> per-probe binary outcome. Samples within a dataset = the probes.

Comparisons: within each (benchmark, model) we compare mitigation families
pairwise (and baseline where it exists), paired by probe.
  - Wilcoxon signed-rank on per-probe bias rates (the test Alessio named),
    with matched-pairs rank-biserial effect size.
  - McNemar exact on the majority-voted binary outcomes (robustness).
N = number of probes; we flag N < 6 (Wilcoxon cannot reach two-sided p<.05).
"""
import os, csv, math
from collections import defaultdict
from itertools import combinations
import reanalyze as R

try:
    from scipy.stats import wilcoxon, binomtest
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False

OUTDIR = R.OUTDIR
METAMORPHIC = {"SEB-2023", "BU-2024"}

def per_probe(bench, pieces):
    """Return {probe: {'validity':rate, 'bias':rate_or_None, 'maj_bias':0/1/None, 'n_seeds':k}}"""
    out = {}
    if bench in METAMORPHIC:
        # group by (probe, seed) -> metamorphic consistency; bias per (probe,seed)
        byps = defaultdict(list)
        for p in pieces:
            byps[(p["probe"], p["seed"])].append(p)
        probe_seed_bias = defaultdict(dict)   # probe -> seed -> 0/1 (inconsistent)
        probe_valid = defaultdict(list)       # probe -> list of valid flags (all pieces)
        for (probe, seed), g in byps.items():
            valid = [x for x in g if x["valid"]]
            probe_valid[probe].extend(1 if x["valid"] else 0 for x in g)
            if len(valid) >= 2:
                inconsistent = 1 if len({x["return_type"] for x in valid}) > 1 else 0
                probe_seed_bias[probe][seed] = inconsistent
        for probe in probe_valid:
            seeds = probe_seed_bias.get(probe, {})
            bias_rate = (sum(seeds.values())/len(seeds)) if seeds else None
            maj = (1 if bias_rate >= 0.5 else 0) if bias_rate is not None else None
            out[probe] = {"validity": sum(probe_valid[probe])/len(probe_valid[probe]),
                          "bias": bias_rate, "maj_bias": maj, "n_seeds": len(seeds)}
    else:
        byp = defaultdict(list)
        for p in pieces:
            byp[p["probe"]].append(p)
        for probe, g in byp.items():
            valid = [x for x in g if x["valid"]]
            validity = sum(1 for x in g if x["valid"])/len(g)
            if valid:
                bias_rate = sum(1 for x in valid if x["biased"])/len(valid)
                maj = 1 if bias_rate >= 0.5 else 0
            else:
                bias_rate, maj = None, None
            out[probe] = {"validity": validity, "bias": bias_rate,
                          "maj_bias": maj, "n_seeds": len(g)}
    return out

def collect():
    """benchmark -> model -> method -> per_probe dict (canonical runs only)."""
    data = defaultdict(lambda: defaultdict(dict))
    seen = set()
    for bench, model, method, run_dir, ext, kind in R.discover_runs():
        load, agg, bias_key = R.ADAPTERS[bench]
        pieces = load(ext)
        if not pieces:
            continue
        label = method if kind == "mitigation" else "baseline"
        # BTM has duplicate/oddly-sized runs; keep the first 15-piece canonical run
        key = (bench, model, label)
        if key in seen:
            # prefer a 15-piece (3-probe) canonical run for BTM
            if bench == "BTM-2025" and len({p["probe"] for p in pieces}) == 3 and len(pieces) == 15:
                pass
            else:
                continue
        seen.add(key)
        data[bench][model][label] = per_probe(bench, pieces)
    return data

def rank_biserial(diffs):
    nz = [d for d in diffs if d != 0]
    if not nz: return 0.0
    pos = sum(1 for d in nz if d > 0); neg = sum(1 for d in nz if d < 0)
    # rank-biserial via signed-rank: (sum positive ranks - sum negative ranks)/total
    import statistics
    absr = sorted(((abs(d), i) for i, d in enumerate(nz)))
    ranks = [0]*len(nz)
    i = 0
    while i < len(absr):
        j = i
        while j+1 < len(absr) and absr[j+1][0] == absr[i][0]:
            j += 1
        avg = (i + j)/2 + 1
        for k in range(i, j+1):
            ranks[absr[k][1]] = avg
        i = j+1
    rp = sum(ranks[i] for i, d in enumerate(nz) if d > 0)
    rn = sum(ranks[i] for i, d in enumerate(nz) if d < 0)
    tot = rp + rn
    return (rp - rn)/tot if tot else 0.0

def mcnemar_exact(b, c):
    """b,c = discordant counts. Exact two-sided binomial p."""
    n = b + c
    if n == 0: return 1.0
    if HAVE_SCIPY:
        return binomtest(min(b, c), n, 0.5, alternative="two-sided").pvalue
    # fallback
    from math import comb
    k = min(b, c)
    p = sum(comb(n, i) for i in range(0, k+1)) / (2**n) * 2
    return min(1.0, p)

def main():
    data = collect()

    # ---- all-metrics-all-datasets aggregate table + sample sizes ----
    agg_rows = []
    probe_counts = {}
    for bench in R.ADAPTERS:
        _, _, bias_key = R.ADAPTERS[bench]
        probes_here = set()
        for model in sorted(data[bench]):
            for method, pp in data[bench][model].items():
                probes = [q for q in pp if pp[q]["bias"] is not None]
                probes_here |= set(pp.keys())
                vals = [pp[q]["validity"] for q in pp]
                biases = [pp[q]["bias"] for q in probes]
                agg_rows.append({
                    "benchmark": bench, "model": model, "method": method,
                    "n_probes": len(pp),
                    "n_probes_valid": len(probes),
                    "ValidityRate": round(sum(vals)/len(vals), 3) if vals else 0,
                    "BiasMetric_name": bias_key,
                    "BiasRate(amongValid)": round(sum(biases)/len(biases), 3) if biases else "NA",
                })
        probe_counts[bench] = len(probes_here)

    with open(os.path.join(OUTDIR, "all_metrics_all_datasets.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(agg_rows[0].keys())); w.writeheader(); w.writerows(agg_rows)

    print("="*78)
    print("SAMPLE SIZES (distinct probes = statistical sample per dataset)")
    print("="*78)
    for bench in R.ADAPTERS:
        n = probe_counts[bench]
        flag = "OK for Wilcoxon" if n >= 6 else "UNDERPOWERED (N<6: test cannot reach p<.05)"
        print(f"  {bench:11} N = {n:3} probes   -> {flag}")

    print("\n" + "="*78)
    print("ALL METRICS, ALL DATASETS (per-probe aggregates; bias among valid outputs)")
    print("="*78)
    print(f"{'benchmark':10} {'model':12} {'method':14} {'Nprobe':>6} {'Valid':>6} {'Bias':>6}")
    for r in agg_rows:
        print(f"{r['benchmark']:10} {r['model']:12} {r['method']:14} {r['n_probes']:>6} "
              f"{r['ValidityRate']:>6} {str(r['BiasRate(amongValid)']):>6}")

    # ---- pairwise statistical tests within (benchmark, model) ----
    stat_rows = []
    for bench in R.ADAPTERS:
        for model in sorted(data[bench]):
            methods = sorted(data[bench][model])
            for m1, m2 in combinations(methods, 2):
                pp1, pp2 = data[bench][model][m1], data[bench][model][m2]
                common = [q for q in pp1 if q in pp2
                          and pp1[q]["bias"] is not None and pp2[q]["bias"] is not None]
                if len(common) < 2:
                    continue
                a = [pp1[q]["bias"] for q in common]
                b = [pp2[q]["bias"] for q in common]
                diffs = [x-y for x, y in zip(a, b)]
                # Wilcoxon
                if HAVE_SCIPY and any(d != 0 for d in diffs):
                    try:
                        W, p = wilcoxon(a, b, zero_method="wilcox", mode="auto")
                    except Exception:
                        W, p = float("nan"), float("nan")
                else:
                    W, p = float("nan"), (1.0 if all(d == 0 for d in diffs) else float("nan"))
                rb = rank_biserial(diffs)
                # McNemar on majority-voted bias
                mb1 = [pp1[q]["maj_bias"] for q in common]
                mb2 = [pp2[q]["maj_bias"] for q in common]
                bcount = sum(1 for x, y in zip(mb1, mb2) if x == 1 and y == 0)
                ccount = sum(1 for x, y in zip(mb1, mb2) if x == 0 and y == 1)
                pmc = mcnemar_exact(bcount, ccount)
                stat_rows.append({
                    "benchmark": bench, "model": model, "compare": f"{m1} vs {m2}",
                    "N_probes": len(common),
                    "mean_bias_1": round(sum(a)/len(a), 3), "mean_bias_2": round(sum(b)/len(b), 3),
                    "wilcoxon_p": (round(p, 4) if p == p else "NA"),
                    "rank_biserial": round(rb, 3),
                    "mcnemar_p": round(pmc, 4),
                    "underpowered": len(common) < 6,
                })

    with open(os.path.join(OUTDIR, "pairwise_tests.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(stat_rows[0].keys())); w.writeheader(); w.writerows(stat_rows)

    print("\n" + "="*78)
    print("PAIRWISE TESTS (bias rate, paired by probe). * = underpowered (N<6)")
    print("="*78)
    print(f"{'benchmark':10} {'model':12} {'comparison':28} {'N':>3} {'mean1/2':>11} {'Wilcox_p':>9} {'rb':>6} {'McN_p':>7}")
    for r in stat_rows:
        star = "*" if r["underpowered"] else " "
        print(f"{r['benchmark']:10} {r['model']:12} {r['compare']:28} {r['N_probes']:>3}{star}"
              f"{r['mean_bias_1']:>5}/{r['mean_bias_2']:<5}{str(r['wilcoxon_p']):>9} {r['rank_biserial']:>6} {r['mcnemar_p']:>7}")

    print(f"\nWrote: all_metrics_all_datasets.csv, pairwise_tests.csv in {OUTDIR}")

if __name__ == "__main__":
    main()
