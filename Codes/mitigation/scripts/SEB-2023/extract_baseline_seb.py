import json, os, glob
import ast as python_ast
from extract_ast import extract_seb_ast
from seb_metrics import compute_seb_metrics

def normalize_code(code_string):
    """Aggressively normalize code by finding the first def and stripping trailing junk."""
    lines = code_string.splitlines()
    
    # Find the first line starting with 'def '
    first_def_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("def "):
            first_def_idx = i
            break
    
    if first_def_idx == -1:
        return code_string
    
    candidate_lines = lines[first_def_idx:]
    
    # Try parsing, if failure, keep removing the last line until it parses or we run out
    current_lines = list(candidate_lines)
    while current_lines:
        try:
            code = "\n".join(current_lines)
            python_ast.parse(code)
            return code
        except SyntaxError:
            current_lines.pop()
    
    return "\n".join(candidate_lines)

baseline_id = "SEB-2023_codegen350M_baseline_20260219_175707"
gen_dir = f"Codes/outputs/SEB-2023/baseline/runs/{baseline_id}/generated"
metrics_dir = "Codes/outputs/SEB-2023/metrics"
os.makedirs(metrics_dir, exist_ok=True)

gen_files = sorted(glob.glob(os.path.join(gen_dir, "*.py")))
print(f"Found {len(gen_files)} baseline generated files.")

all_extractions = []
for gf in gen_files:
    with open(gf) as f:
        code = f.read()
    
    # Normalize baseline code to remove echo preambles and trailing junk
    norm_code = normalize_code(code)
    ext = extract_seb_ast(norm_code)
    
    bn = os.path.basename(gf)
    ext["task_id"] = "check_even"
    ext["seed"] = 1
    for v in ["base", "short", "formal", "implied"]:
        if f"_{v}_" in bn or bn.endswith(f"_{v}.py"):
            ext["variant_id"] = v
            break
    else:
        ext["variant_id"] = "unknown"
    ext["file"] = gf
    all_extractions.append(ext)
    print(f"  {bn}: parse_ok={ext['parse_ok']}, return_type={ext['return_type']}")

metrics = compute_seb_metrics(all_extractions, len(gen_files))
mf = os.path.join(metrics_dir, "SEB-2023_codegen350M_baseline_metrics.json")
with open(mf, "w") as f:
    json.dump(metrics, f, indent=2)
print(f"\nBaseline metrics (Recovered): {json.dumps(metrics, indent=2)}")
