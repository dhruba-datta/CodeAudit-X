#!/usr/bin/env python3
"""
Merge a Kaggle regeneration run (Phase 5b, "authors' metrics") into runs/.

The regeneration produced three things, each handled differently:

  BTM-2025   only promptmit_v1 was regenerated (the old v1 was a silent no-op,
             see prompts.py). Every promptmit_v1 record in the study shards is
             REPLACED by its regenerated twin, keyed by job_id. baseline and
             promptmit_v2 records are untouched. A backup of each touched shard
             is written next to it as *.jsonl.pre-v1fix.
  BU-2024A   new benchmark, no prior records: copied in as-is.
  UQSB-2023  regenerated only so the classifier could score it on Kaggle. The
             study's UQSB generations are NOT replaced. Instead we report how
             many regenerated records are byte-identical to the study's, per
             model, so the classifier numbers can be read against the study.
             Pass --replace-uqsb to overwrite anyway.

Usage:
  tar xzf runs_authors_metrics.tar.gz -C /tmp/regen
  python merge_regen.py --src /tmp/regen/runs
"""
import argparse
import json
import shutil
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"


def read(path):
    rows = []
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return rows


def write(path, rows):
    with path.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")


def merge_btm(src):
    total_replaced = 0
    for new_path in sorted((src / "BTM-2025").glob("*.jsonl")):
        old_path = RUNS / "BTM-2025" / new_path.name
        new_rows = [r for r in read(new_path) if r["method"] == "promptmit_v1"]
        new_by_id = {r["job_id"]: r for r in new_rows}
        if not old_path.exists():
            print(f"[btm ] {new_path.name}: no study shard, copying {len(new_rows)} v1 records")
            old_path.parent.mkdir(parents=True, exist_ok=True)
            write(old_path, new_rows)
            continue
        old_rows = read(old_path)
        keep = [r for r in old_rows if r["method"] != "promptmit_v1"]
        dropped = len(old_rows) - len(keep)
        missing = {r["job_id"] for r in old_rows if r["method"] == "promptmit_v1"} - set(new_by_id)
        if missing:
            print(f"[btm ] WARNING {new_path.name}: {len(missing)} old v1 job_ids not regenerated "
                  f"(e.g. {sorted(missing)[:3]}); keeping their OLD records")
            keep += [r for r in old_rows if r["job_id"] in missing]
        backup = old_path.with_suffix(".jsonl.pre-v1fix")
        if not backup.exists():
            shutil.copy2(old_path, backup)
        write(old_path, keep + new_rows)
        total_replaced += dropped
        print(f"[btm ] {new_path.name}: dropped {dropped} old v1, added {len(new_rows)} new v1, "
              f"now {len(keep) + len(new_rows)} records (backup: {backup.name})")
    print(f"[btm ] replaced {total_replaced} promptmit_v1 records in total")


def copy_bu2024a(src):
    d = src / "BU-2024A"
    if not d.exists():
        print("[bu-a] nothing to copy")
        return
    (RUNS / "BU-2024A").mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted(d.glob("*.jsonl")):
        shutil.copy2(p, RUNS / "BU-2024A" / p.name)
        n += len(read(p))
    print(f"[bu-a] copied {n} BU-2024A records")


def compare_uqsb(src, replace=False):
    d = src / "UQSB-2023"
    if not d.exists():
        print("[uqsb] nothing regenerated")
        return
    per_model = defaultdict(Counter)
    for new_path in sorted(d.glob("*.jsonl")):
        old_path = RUNS / "UQSB-2023" / new_path.name
        new_rows = read(new_path)
        if not old_path.exists():
            print(f"[uqsb] {new_path.name}: no study shard to compare against")
            if replace:
                old_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(new_path, old_path)
            continue
        old_by_id = {r["job_id"]: r for r in read(old_path)}
        for r in new_rows:
            o = old_by_id.get(r["job_id"])
            c = per_model[r["model"]]
            c["n"] += 1
            if o is None:
                c["unmatched"] += 1
            elif (o.get("raw") or "") == (r.get("raw") or ""):
                c["identical_raw"] += 1
        if replace:
            backup = old_path.with_suffix(".jsonl.pre-regen")
            if not backup.exists():
                shutil.copy2(old_path, backup)
            shutil.copy2(new_path, old_path)
    print("[uqsb] regenerated vs study, per model:")
    for m, c in sorted(per_model.items()):
        print(f"       {m:<13} n={c['n']:>6}  identical raw={c['identical_raw']:>6} "
              f"({c['identical_raw'] / max(c['n'], 1):.1%})  unmatched={c['unmatched']}")
    print("       (agreement < 100% is expected: same seed on the same T4 is usually but not "
          "always bit-reproducible under vLLM batching. Report the figure.)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="the regeneration's runs/ directory")
    ap.add_argument("--replace-uqsb", action="store_true")
    args = ap.parse_args()
    src = Path(args.src).resolve()
    if not src.exists():
        raise SystemExit(f"{src} does not exist")
    merge_btm(src)
    copy_bu2024a(src)
    compare_uqsb(src, args.replace_uqsb)
    print("\nnext: python extract_and_score.py && python metrics_btm_authors.py")


if __name__ == "__main__":
    main()
