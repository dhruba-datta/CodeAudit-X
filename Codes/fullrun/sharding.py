#!/usr/bin/env python3
"""
CodeAudit-X full run: stratified sharding.

Splits each benchmark's full probe set into N chunks that can be generated
independently, on different days or different machines.

WHY THE SHARDS ARE STRATIFIED
-----------------------------
The naive way to chunk a dataset is to slice it into contiguous blocks. Don't.
The full probe sets are built by crossing dimensions (task x phrasing,
adjective x protected attribute, HumanEval then MBPP), so a contiguous block is
systematically skewed -- shard 0 of UQSB-2023 would be entirely `ethnicity`,
shard 6 entirely `disability`.

Here every shard is a proportional sample of every stratum. Consequences:

  * Stop after shard 0 and you hold a statistically representative subsample of
    the full benchmark, not an arbitrary prefix. That is a defensible answer to
    "why only a subset?" in a way hand-curation never was.
  * Run shards 0..k and the sample stays representative as it grows.
  * Run all N and you have the complete dataset, partitioned exactly once --
    no probe appears twice, none is dropped.

Sharding happens at PROBE level, never at generation level. Every method, seed
and variant of a probe stays in the same shard, because SEB-2023 and BU-2024
compute bias by comparing variants of one probe against each other, and the
paired McNemar tests compare methods on the same (probe, seed). Splitting a
probe across shards would silently destroy both.

Stratification key per benchmark:
  BTM-2025   task            (48 decision tasks, 7 phrasings each)
  UQSB-2023  attribute       (7 protected attributes, 56 adjectives each)
  SEB-2023   source          (HumanEval vs MBPP)
  BU-2024    -               (tasks are homogeneous; seeded round-robin)
  IMSB-2025  type            (gender / race / religion)
"""
import copy
import json
import random
from collections import Counter, defaultdict

# Where each benchmark keeps its probe list, and how to stratify it.
PROBE_LIST_KEY = {
    "BTM-2025": "prompts",
    "UQSB-2023": "probes",
    "SEB-2023": "probes",
    "BU-2024": "tasks",
    "IMSB-2025": "triplets",
}

STRATUM_FIELD = {
    "BTM-2025": "task",
    "UQSB-2023": "attribute",
    "SEB-2023": "source",
    "BU-2024": None,          # homogeneous role-suitability tasks
    "IMSB-2025": "type",
}

# Fixed so shard membership is reproducible across machines and reruns. Changing
# it repartitions everything and invalidates any partial run already on disk.
SHARD_SEED = 20260827


def stratum_of(benchmark, probe):
    field = STRATUM_FIELD.get(benchmark)
    if field is None:
        return "_all"
    return str(probe.get(field, "_unknown"))


def assign(benchmark, spec, n_shards):
    """Return list[list[probe]] of length n_shards, proportional per stratum."""
    if n_shards < 1:
        raise ValueError("n_shards must be >= 1")
    probes = spec[PROBE_LIST_KEY[benchmark]]
    if n_shards == 1:
        return [list(probes)]

    by_stratum = defaultdict(list)
    for p in probes:
        by_stratum[stratum_of(benchmark, p)].append(p)

    shards = [[] for _ in range(n_shards)]
    rng = random.Random(SHARD_SEED)
    # Offset the round-robin start per stratum so that when a stratum is smaller
    # than n_shards its members don't all pile into the low-numbered shards.
    for si, stratum in enumerate(sorted(by_stratum)):
        members = list(by_stratum[stratum])
        rng.shuffle(members)
        for i, p in enumerate(members):
            shards[(i + si) % n_shards].append(p)
    return shards


def slice_spec(benchmark, spec, shard_idx, n_shards):
    """A copy of `spec` holding only shard `shard_idx` of `n_shards`."""
    shards = assign(benchmark, spec, n_shards)
    if not 0 <= shard_idx < n_shards:
        raise ValueError(f"shard index {shard_idx} out of range for {n_shards} shards")
    out = copy.copy(spec)
    out[PROBE_LIST_KEY[benchmark]] = shards[shard_idx]
    out["_shard"] = {"index": shard_idx, "of": n_shards, "seed": SHARD_SEED,
                     "stratified_by": STRATUM_FIELD.get(benchmark),
                     "n_probes": len(shards[shard_idx])}
    return out


MAX_STRATA_COLUMNS = 8


def report(benchmark, spec, n_shards):
    """Human-readable composition: rows = shards, cols = strata.

    Benchmarks with many strata (BTM-2025 has 48 tasks) get a condensed view
    instead of a 48-column table nobody can read.
    """
    shards = assign(benchmark, spec, n_shards)
    strata = sorted({stratum_of(benchmark, p)
                     for p in spec[PROBE_LIST_KEY[benchmark]]})
    total = Counter(stratum_of(benchmark, p)
                    for p in spec[PROBE_LIST_KEY[benchmark]])
    field = STRATUM_FIELD.get(benchmark) or "-"

    if len(strata) > MAX_STRATA_COLUMNS:
        lines = [f"{benchmark}  ({sum(total.values())} probes, {n_shards} shards, "
                 f"stratified by {field} -- {len(strata)} strata, condensed)"]
        lines.append("  shard  probes  strata covered  min/stratum  max/stratum")
        for i, sh in enumerate(shards):
            c = Counter(stratum_of(benchmark, p) for p in sh)
            per = [c.get(s, 0) for s in strata]
            lines.append(f"  {i:>5}  {len(sh):>6}  {sum(1 for v in per if v):>14}"
                         f"  {min(per):>11}  {max(per):>11}")
        lines.append(f"  TOTAL  {sum(total.values()):>6}  {len(strata):>14}"
                     f"  {min(total.values()):>11}  {max(total.values()):>11}")
        return "\n".join(lines)

    w = max([len(s) for s in strata] + [7])
    lines = [f"{benchmark}  ({sum(total.values())} probes, {n_shards} shards, "
             f"stratified by {field})"]
    lines.append("  shard  " + "  ".join(f"{s:>{w}}" for s in strata) + "    total")
    for i, sh in enumerate(shards):
        c = Counter(stratum_of(benchmark, p) for p in sh)
        lines.append(f"  {i:>5}  " + "  ".join(f"{c.get(s, 0):>{w}}" for s in strata)
                     + f"    {len(sh):>5}")
    lines.append("  " + "-" * (7 + (w + 2) * len(strata) + 9))
    lines.append("  TOTAL  " + "  ".join(f"{total[s]:>{w}}" for s in strata)
                 + f"    {sum(total.values()):>5}")
    return "\n".join(lines)


def verify(benchmark, spec, n_shards):
    """Assert the shards partition the probe set exactly once. Returns stats."""
    probes = spec[PROBE_LIST_KEY[benchmark]]
    shards = assign(benchmark, spec, n_shards)
    flat = [json.dumps(p, sort_keys=True) for sh in shards for p in sh]
    original = [json.dumps(p, sort_keys=True) for p in probes]

    dupes = len(flat) - len(set(flat))
    missing = set(original) - set(flat)
    extra = set(flat) - set(original)
    sizes = [len(sh) for sh in shards]

    # Per-stratum proportionality: no shard may deviate from the expected share
    # of any stratum by more than one probe (integer rounding).
    total = Counter(stratum_of(benchmark, p) for p in probes)
    worst = 0.0
    for i, sh in enumerate(shards):
        c = Counter(stratum_of(benchmark, p) for p in sh)
        for s, n in total.items():
            worst = max(worst, abs(c.get(s, 0) - n / n_shards))

    return {"benchmark": benchmark, "n_shards": n_shards, "n_probes": len(probes),
            "shard_sizes": sizes, "duplicates": dupes, "missing": len(missing),
            "extra": len(extra), "max_stratum_deviation": round(worst, 3),
            "ok": dupes == 0 and not missing and not extra and worst <= 1.0}
