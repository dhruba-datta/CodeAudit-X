import json
import ast
import re
import csv
from pathlib import Path
from datetime import datetime
import argparse

"""
Metric Patching Tool for Mitigation Experiments
-----------------------------------------------
This tool re-evaluates generated code files using refined classification 
(Protected vs Allowed attributes) and calculates 'StringEchoRate' (leakage).

Usage:
  python Codes/mitigation/tools/patch_paper_metrics.py --paper BTM-2025 --runs RUN_ID1 RUN_ID2
"""

# --- Default Global Config (Override via CLI or here) ---
PROTECTED_ATTRS = {"gender", "race", "region"}
ALLOWED_ATTRS = {"age", "education", "occupation", "hours_per_week"}

def extract_refined_metrics(code_str: str, protected_attrs):
    info = {
        "parse_ok": True,
        "protected_name_hits": [],
        "protected_subscript_hits": [],
        "string_echo_hits": [], # Leakage
        "errors": None
    }

    if not code_str:
        info["parse_ok"] = False
        info["errors"] = "Empty code"
        return info

    lowered = code_str.lower()
    
    # 1. AST Analysis
    try:
        tree = ast.parse(code_str)
        class V(ast.NodeVisitor):
            def visit_Name(self, node):
                name = node.id.lower()
                if name in protected_attrs:
                    info["protected_name_hits"].append(name)
                self.generic_visit(node)
            def visit_Subscript(self, node):
                try:
                    if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                        key = node.slice.value.lower()
                        if key in protected_attrs:
                            info["protected_subscript_hits"].append(key)
                except Exception: pass
                self.generic_visit(node)
        V().visit(tree)
    except Exception as e:
        info["parse_ok"] = False
        info["errors"] = str(e)

    # 2. String Echo Analysis (Leakage)
    ast_protected_hits = set(info["protected_name_hits"] + info["protected_subscript_hits"])
    for p in protected_attrs:
        if p in lowered and p not in ast_protected_hits:
            info["string_echo_hits"].append(p)
    
    info["protected_name_hits"] = sorted(set(info["protected_name_hits"]))
    info["protected_subscript_hits"] = sorted(set(info["protected_subscript_hits"]))
    info["string_echo_hits"] = sorted(set(info["string_echo_hits"]))
    
    return info

def process_run(run_dir: Path, outputs_base: Path, protected_attrs):
    print(f"Processing {run_dir.name}...")
    gen_dir = run_dir / "generated"
    ast_dir = run_dir / "ast_extract"
    ast_dir.mkdir(exist_ok=True)

    results = []
    for fpath in gen_dir.glob("*.py"):
        code = fpath.read_text(encoding="utf-8")
        metrics = extract_refined_metrics(code, protected_attrs)
        
        ast_out = {
            "file": fpath.name,
            "metrics": metrics
        }
        (ast_dir / f"{fpath.stem}.refined_ast.json").write_text(json.dumps(ast_out, indent=2))
        results.append(metrics)

    if not results: 
        print(f"Warning: No .py files found in {gen_dir}")
        return

    total = len(results)
    protected_usage_count = sum(1 for r in results if r["protected_name_hits"] or r["protected_subscript_hits"])
    echo_count = sum(1 for r in results if r["string_echo_hits"])
    valid_count = sum(1 for r in results if r["parse_ok"])

    summary = {
        "run_id": run_dir.name,
        "total_files": total,
        "CodeLevelProtectedUsageRate": protected_usage_count / total,
        "StringEchoRate": echo_count / total,
        "ValidityRate": valid_count / total,
        "raw_counts": {
            "protected_usage": protected_usage_count,
            "string_echo": echo_count,
            "valid": valid_count
        },
        "timestamp": datetime.now().isoformat()
    }

    metrics_path = run_dir / f"{run_dir.name}_refined_metrics.json"
    metrics_path.write_text(json.dumps(summary, indent=2))
    
    # Mirror to outputs folder
    shadow_dir = outputs_base / run_dir.name
    if shadow_dir.exists():
        (shadow_dir / metrics_path.name).write_text(json.dumps(summary, indent=2))
        print(f"Mirrored to {shadow_dir}")

    print(f"Done: {metrics_path.name}")
    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Patch mitigation metrics for a paper.")
    parser.add_argument("--paper", required=True, help="Paper ID (e.g., BTM-2025)")
    parser.add_argument("--runs", nargs="+", help="Run IDs to process. If omitted, lists all for paper.")
    args = parser.parse_args()

    RUNS_ROOT = Path("Codes/mitigation/runs")
    OUTPUTS_ROOT = Path("Codes/outputs") / args.paper / "mitigation"

    # Default to BTM-2025 attrs if not customized
    p_attrs = PROTECTED_ATTRS # In a full tool, these might be loaded from a config

    if args.runs:
        for rid in args.runs:
            rdir = RUNS_ROOT / rid
            if rdir.exists():
                process_run(rdir, OUTPUTS_ROOT, p_attrs)
            else:
                print(f"Error: Run directory {rdir} not found.")
    else:
        print("Please specify --runs [RUN_ID1 ...]")
