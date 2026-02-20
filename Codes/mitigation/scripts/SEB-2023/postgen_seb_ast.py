"""
Post-generation normalization for SEB-2023.
Strips trailing code after the first function to improve structural consistency.
"""
import json, os, re, shutil, datetime
from pathlib import Path
from extract_ast import extract_seb_ast
from seb_metrics import compute_seb_metrics
import ast as python_ast

def normalize_code(code_string):
    """Keep only the first function definition, remove trailing code."""
    try:
        tree = python_ast.parse(code_string)
    except SyntaxError:
        return code_string

    functions = [n for n in python_ast.iter_child_nodes(tree)
                 if isinstance(n, python_ast.FunctionDef)]
    if not functions:
        return code_string

    first_fn = functions[0]
    # Find the end line of the first function
    end_line = first_fn.end_lineno if hasattr(first_fn, 'end_lineno') and first_fn.end_lineno else None
    if end_line is None:
        return code_string

    lines = code_string.splitlines()
    # Keep lines up to and including the first function, plus any leading comments/imports
    start_line = first_fn.lineno
    prefix_lines = lines[:start_line - 1]
    fn_lines = lines[start_line - 1:end_line]

    # Filter prefix to only keep comments and blank lines
    clean_prefix = [l for l in prefix_lines if l.strip() == '' or l.strip().startswith('#')]
    return '\n'.join(clean_prefix + fn_lines) + '\n'

def run_postgen(config_path):
    with open(config_path) as f:
        config = json.load(f)

    source_run_id = config["source_run_id"]
    model_tag = config["model_tag"]
    source_dir = Path(f"Codes/mitigation/runs/{source_run_id}")
    gen_dir = source_dir / "generated"

    if not gen_dir.exists():
        print(f"ERROR: Source dir not found: {gen_dir}")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"SEB-2023_{model_tag}_postgenast_v1_{timestamp}"
    run_dir = Path(f"Codes/mitigation/runs/{run_id}")
    scrub_gen_dir = run_dir / "generated"
    ast_dir = run_dir / "ast_extract"
    scrub_gen_dir.mkdir(parents=True, exist_ok=True)
    ast_dir.mkdir(parents=True, exist_ok=True)

    print(f"Starting Post-Gen Normalization: {run_id}")
    source_files = sorted(gen_dir.glob("*.py"))
    print(f"Normalizing {len(source_files)} files from {source_run_id}...")

    all_extractions = []
    total = len(source_files)

    for src_file in source_files:
        with open(src_file) as f:
            original = f.read()

        normalized = normalize_code(original)
        out_file = scrub_gen_dir / src_file.name
        with open(out_file, "w") as f:
            f.write(normalized)

        ext = extract_seb_ast(normalized)
        # Parse task_id and variant from filename
        parts = src_file.stem.split('_')
        # SEB-2023_<model>_<task>_<variant>_<version>_seed<n>
        task_id = None
        variant_id = None
        seed = 0
        for i, p in enumerate(parts):
            if p.startswith("seed"):
                seed = int(p.replace("seed", ""))
            if p in ("check", "find", "reverse"):
                task_id = '_'.join(parts[i:i+2]) if i+1 < len(parts) and parts[i+1] in ("even", "max", "string") else p
            if p in ("base", "short", "formal", "implied"):
                variant_id = p

        ext["task_id"] = task_id or "unknown"
        ext["variant_id"] = variant_id or "unknown"
        ext["seed"] = seed
        ext["source_file"] = str(src_file)

        ast_file = ast_dir / (src_file.stem + ".ast.json")
        with open(ast_file, "w") as f:
            json.dump(ext, f, indent=2)

        all_extractions.append(ext)

    metrics = compute_seb_metrics(all_extractions, total)
    metrics_file = run_dir / f"{run_id}_refined_metrics.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=2)

    mirror_dir = Path(f"Codes/outputs/SEB-2023/mitigation/{run_id}")
    if mirror_dir.exists(): shutil.rmtree(mirror_dir)
    shutil.copytree(run_dir, mirror_dir)
    print(f"Mirroring to {mirror_dir}")

    pbr = metrics.get("PerturbationBiasRate", "NA")
    pbr_str = f"{pbr:.4f}" if isinstance(pbr, (int, float)) else pbr
    print(f"Postgen complete. PerturbationBiasRate: {pbr_str}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python postgen_seb_ast.py <config_path>")
        sys.exit(1)
    run_postgen(sys.argv[1])
