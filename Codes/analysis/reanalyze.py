#!/usr/bin/env python3
"""
CodeAudit-X re-analysis pipeline (no model inference required).

Purpose (addresses Alessio's review):
  - Move the unit of analysis from the benchmark to the individual code piece
    (probe x seed), so per-dataset statistics become possible.
  - Recompute every run's aggregate from the per-piece data and VALIDATE it
    against the frozen *_metrics.json, so the per-probe table is provably the
    same data behind the frozen results.

Stage 1 (this file): load + per-piece extraction + aggregate recompute +
validation against stored metrics + long-format CSV dump.

Reads only existing run artifacts under Codes/mitigation/runs and
Codes/outputs/<P>/baseline/runs. Writes only under Codes/analysis/out.
"""
import json, glob, os, csv, sys, re
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUNS = os.path.join(ROOT, "Codes", "mitigation", "runs")
OUTPUTS = os.path.join(ROOT, "Codes", "outputs")
OUTDIR = os.path.join(ROOT, "Codes", "analysis", "out")
os.makedirs(OUTDIR, exist_ok=True)

BTM_PROTECTED = {"gender", "race", "region"}

# ---------------------------------------------------------------------------
# Per-benchmark adapters.
# Each returns a list of per-piece dicts: {probe, variant, seed, valid, biased}
# where `biased` may be None for metamorphic benchmarks (bias is per-group, set
# later) and `valid` is parse_ok. `aggregate(pieces)` recomputes the benchmark's
# headline metrics so we can validate against the frozen metrics file.
# ---------------------------------------------------------------------------

def _seed_from_name(name):
    m = re.search(r"seed[_-]?(\d+)|_s(\d+)\b", name)
    if m:
        return int(m.group(1) or m.group(2))
    return None

def load_imsb(ext_dir):
    pieces = []
    for fp in glob.glob(os.path.join(ext_dir, "*.json")):
        d = json.load(open(fp))
        pieces.append({
            "probe": d.get("task_id", "?"),
            "variant": None,
            "seed": d.get("seed"),
            "valid": bool(d.get("parse_ok", False)),
            "biased": bool(d.get("reinforces_bias", False)) if d.get("parse_ok") else None,
        })
    return pieces

def agg_imsb(pieces):
    valid = [p for p in pieces if p["valid"]]
    n = len(pieces)
    return {
        "ValidityRate": round(len(valid)/n, 4) if n else 0.0,
        "BiasKnowledgeRate": round(sum(1 for p in valid if p["biased"])/len(valid), 4) if valid else "NA",
    }

def load_uqsb(ext_dir):
    pieces = []
    for fp in glob.glob(os.path.join(ext_dir, "*.json")):
        d = json.load(open(fp))
        probe = d.get("probe_id")
        seed = d.get("seed")
        if probe is None:
            base = os.path.basename(d.get("source_file") or d.get("scrubbed_file") or fp)
            seed = seed if seed is not None else _seed_from_name(base)
            probe = re.sub(r"^UQSB-2023_[a-z0-9.]+_", "", base)
            probe = re.sub(r"_seed\d+.*$", "", probe)
        pieces.append({
            "probe": probe, "variant": None, "seed": seed,
            "valid": bool(d.get("parse_ok", False)),
            "biased": bool(d.get("uses_sensitive_in_logic", False)) if d.get("parse_ok") else None,
        })
    return pieces

def agg_uqsb(pieces):
    valid = [p for p in pieces if p["valid"]]
    n = len(pieces)
    return {
        "ValidityRate": round(len(valid)/n, 4) if n else 0.0,
        "ContextBiasRate": round(sum(1 for p in valid if p["biased"])/len(valid), 4) if valid else "NA",
    }

def _meta_pieces(ext_dir):
    pieces = []
    for fp in glob.glob(os.path.join(ext_dir, "*.json")):
        d = json.load(open(fp))
        pieces.append({
            "probe": d.get("task_id", "?"),
            "variant": d.get("variant_id"),
            "seed": d.get("seed"),
            "valid": bool(d.get("parse_ok", False)),
            "return_type": d.get("return_type", "unknown"),
            "biased": None,  # group-level
        })
    return pieces

load_seb = _meta_pieces
load_bu = _meta_pieces

def _meta_agg(pieces, bias_key):
    valid = [p for p in pieces if p["valid"]]
    n = len(pieces)
    groups = defaultdict(list)
    for p in valid:
        groups[(p["probe"], p["seed"])].append(p)
    inconsistent = total = 0
    for g in groups.values():
        if len(g) < 2:
            continue
        total += 1
        if len({p["return_type"] for p in g}) > 1:
            inconsistent += 1
    rate = round(inconsistent/total, 4) if total else "NA"
    return {"ValidityRate": round(len(valid)/n, 4) if n else 0.0, bias_key: rate,
            "_groups": total, "_inconsistent": inconsistent}

def agg_seb(pieces):
    a = _meta_agg(pieces, "PerturbationBiasRate"); return a
def agg_bu(pieces):
    a = _meta_agg(pieces, "CodeBiasScore"); return a

def load_btm(ext_dir):
    """Strict, uniform CLPUR: a piece is biased iff a PROTECTED attribute
    (gender/race/region) is used in code (name hit or record indexing /
    subscript), ignoring mere string echo. Handles both BTM schemas:
    baseline/promptmit -> `ast_sensitive_usage`; postgenast -> `metrics`."""
    pieces = []
    for fp in glob.glob(os.path.join(ext_dir, "*.json")):
        d = json.load(open(fp))
        name = d.get("prompt_id") or d.get("file") or os.path.basename(fp)
        m = re.search(r"(AI_\d+)", name)
        probe = m.group(1) if m else name
        # base vs mitigated/v2/v3 phrasing kept as variant for transparency
        vm = re.search(r"AI_\d+_([a-z0-9]+)", name)
        variant = vm.group(1) if vm else None
        seed = d.get("seed")
        if seed is None:
            seed = _seed_from_name(d.get("file") or os.path.basename(fp))
        valid = False; biased = None
        if "ast_sensitive_usage" in d:        # baseline + promptmit
            u = d["ast_sensitive_usage"]
            valid = bool(u.get("parse_ok", False))
            if valid:
                hits = set(map(str.lower, u.get("sensitive_name_hits", []))) \
                     | set(map(str.lower, u.get("uses_record_indexing", [])))
                biased = len(hits & BTM_PROTECTED) > 0
        elif "metrics" in d or "refined_metrics" in d:  # postgenast / deepseek+qwen promptmit
            mtr = d.get("metrics") or d.get("refined_metrics")
            valid = bool(mtr.get("parse_ok", False))
            if valid:
                hits = set(map(str.lower, mtr.get("protected_name_hits", []))) \
                     | set(map(str.lower, mtr.get("protected_subscript_hits", [])))
                biased = len(hits & BTM_PROTECTED) > 0
        pieces.append({"probe": probe, "variant": variant, "seed": seed,
                       "valid": valid, "biased": biased})
    return pieces

def agg_btm(pieces):
    valid = [p for p in pieces if p["valid"]]
    n = len(pieces)
    return {
        "ValidityRate": round(len(valid)/n, 4) if n else 0.0,
        "CodeLevelProtectedUsageRate": round(sum(1 for p in valid if p["biased"])/len(valid), 4) if valid else "NA",
    }

ADAPTERS = {
    "BTM-2025":  (load_btm,  agg_btm,  "CodeLevelProtectedUsageRate"),
    "UQSB-2023": (load_uqsb, agg_uqsb, "ContextBiasRate"),
    "SEB-2023":  (load_seb,  agg_seb,  "PerturbationBiasRate"),
    "BU-2024":   (load_bu,   agg_bu,   "CodeBiasScore"),
    "IMSB-2025": (load_imsb, agg_imsb, "BiasKnowledgeRate"),
}

def find_stored_metrics(run_dir):
    cands = glob.glob(os.path.join(run_dir, "*metrics*.json"))
    for c in cands:
        try:
            return os.path.basename(c), json.load(open(c))
        except Exception:
            continue
    return None, None

def discover_runs():
    """Return list of (benchmark, model, method, run_dir, kind)."""
    runs = []
    # mitigation runs
    for bench in ADAPTERS:
        for run_dir in glob.glob(os.path.join(RUNS, f"{bench}_*")):
            base = os.path.basename(run_dir)
            parts = base.split("_")
            model = parts[1] if len(parts) > 1 else "?"
            method = "_".join(parts[2:-2]) if len(parts) > 4 else "?"
            ext = os.path.join(run_dir, "ast_extract")
            if os.path.isdir(ext):
                runs.append((bench, model, method, run_dir, ext, "mitigation"))
        # codegen baseline (BTM has per-piece extractions)
        for run_dir in glob.glob(os.path.join(OUTPUTS, bench, "baseline", "runs", f"{bench}_*baseline*")):
            ext = os.path.join(run_dir, "ast_extract")
            if os.path.isdir(ext) and glob.glob(os.path.join(ext, "*.json")):
                runs.append((bench, "codegen350M", "baseline", run_dir, ext, "baseline"))
    return runs

def main():
    rows = []          # long-format per-piece
    val_report = []    # validation vs stored metrics
    for bench, model, method, run_dir, ext, kind in discover_runs():
        load, agg, bias_key = ADAPTERS[bench]
        pieces = load(ext)
        if not pieces:
            continue
        recomputed = agg(pieces)
        fname, stored = find_stored_metrics(run_dir)
        srec = {}
        if stored:
            srec = {k: stored.get(k) for k in ("ValidityRate", bias_key)}
        val_report.append({
            "benchmark": bench, "model": model, "method": method, "kind": kind,
            "n_pieces": len(pieces),
            "recomp_validity": recomputed.get("ValidityRate"),
            "stored_validity": srec.get("ValidityRate"),
            "recomp_bias": recomputed.get(bias_key),
            "stored_bias": srec.get(bias_key),
            "metrics_file": fname,
        })
        for p in pieces:
            rows.append({
                "benchmark": bench, "model": model, "method": method, "kind": kind,
                "probe": p["probe"], "variant": p["variant"], "seed": p["seed"],
                "valid": int(p["valid"]),
                "biased": ("" if p["biased"] is None else int(p["biased"])),
            })

    long_csv = os.path.join(OUTDIR, "per_piece_long.csv")
    with open(long_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["benchmark","model","method","kind","probe","variant","seed","valid","biased"])
        w.writeheader(); w.writerows(rows)

    val_csv = os.path.join(OUTDIR, "validation_vs_frozen.csv")
    with open(val_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(val_report[0].keys()))
        w.writeheader(); w.writerows(val_report)

    # console summary
    def close(a, b, tol=0.02):
        try: return abs(float(a)-float(b)) <= tol
        except: return a == b
    print(f"Loaded {len(rows)} per-piece records across {len(val_report)} runs.")
    print(f"Long CSV  -> {long_csv}")
    print(f"Valid CSV -> {val_csv}\n")
    print("VALIDATION (recomputed vs frozen metrics.json):")
    hdr = f"{'benchmark':10} {'model':12} {'method':22} {'n':>3}  {'val(rc/st)':>14}  {'bias(rc/st)':>16}  match"
    print(hdr); print("-"*len(hdr))
    mism = 0
    for r in sorted(val_report, key=lambda x:(x['benchmark'],x['model'],x['method'])):
        vmatch = close(r['recomp_validity'], r['stored_validity']) if r['stored_validity'] is not None else None
        bmatch = close(r['recomp_bias'], r['stored_bias']) if r['stored_bias'] is not None else None
        ok = "n/a" if (vmatch is None and bmatch is None) else ("OK" if (vmatch in (True,None) and bmatch in (True,None)) else "MISMATCH")
        if ok == "MISMATCH": mism += 1
        print(f"{r['benchmark']:10} {r['model']:12} {r['method'][:22]:22} {r['n_pieces']:>3}  "
              f"{str(r['recomp_validity']):>6}/{str(r['stored_validity']):>6}  "
              f"{str(r['recomp_bias']):>7}/{str(r['stored_bias']):>7}  {ok}")
    print(f"\n{mism} mismatches (where a stored metric exists to compare).")

if __name__ == "__main__":
    main()
