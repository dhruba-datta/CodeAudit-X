import json
import ast
import re
import csv
import shutil
import torch
from pathlib import Path
from datetime import datetime
from transformers import pipeline, set_seed

# --- Configuration ---
CONFIG_PATH = Path("Codes/mitigation/configs/FC-2025/fc_prompt_mitigation_deepseek1.3b_v2.json")
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

PAPER_ID = config["paper_id"]
MODEL_NAME = config["model_name"]
MODEL_TAG = config["model_tag"]
DOMAIN = config["domain"]
SEEDS = config["seeds"]
PROMPTS = config["prompts"]

PROTECTED_ATTRS = {"gender", "race", "age"}

PHASE = "mitigation"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_ID = f"{PAPER_ID}_{MODEL_TAG}_promptmit_v2_{TIMESTAMP}"

# --- Paths ---
ROOT = Path.cwd()
MITIGATION_ROOT = ROOT / "Codes" / "mitigation" / "runs" / RUN_ID
GEN_DIR = MITIGATION_ROOT / "generated"
AST_DIR = MITIGATION_ROOT / "ast_extract"
LOG_DIR = MITIGATION_ROOT / "logs"
SHADOW_OUTPUT_DIR = ROOT / "Codes" / "outputs" / PAPER_ID / "mitigation" / RUN_ID

for d in [GEN_DIR, AST_DIR, LOG_DIR, SHADOW_OUTPUT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# --- Model ---
device = "mps" if torch.backends.mps.is_available() else "cpu"
# Fallback to cpu for codegen if mps causes issues, but we'll try mps first
if "deepseek1.3b" == "codegen350M":
    device = "cpu" # codegen fails on some mps ops occasionally

print(f"Loading model: {MODEL_NAME} on {device}")

generator = pipeline(
    "text-generation", 
    model=MODEL_NAME, 
    device=device,
    torch_dtype=torch.bfloat16 if device == "mps" else torch.float32,
    trust_remote_code=True

)

def clean_code(text: str) -> str:
    match = re.search(r"```python\s*(.*?)\s*```", text, re.DOTALL)
    if match: return match.group(1).strip()
    return text.strip()

# --- Execution ---
results_index = []
print(f"Starting {MODEL_TAG} mitigation run: {RUN_ID}")

for p in PROMPTS:
    for seed in SEEDS:
        set_seed(seed)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating for {p['prompt_id']}, seed {seed}...", flush=True)
        
        prompt_text = p["text"]
        
        # Pad token ID setup for deepseek/qwen
        pad_token_id = generator.tokenizer.eos_token_id
        if "deepseek1.3b" == "deepseek1.3b":
            pad_token_id = 50256
            
        out = generator(
            prompt_text,
            max_new_tokens=400,
            do_sample=True,
            temperature=0.4,
            top_p=0.9,
            pad_token_id=pad_token_id
        )

        raw = out[0]["generated_text"]
        
        if raw.startswith(prompt_text):
            completion = raw[len(prompt_text):].strip()
        else:
            completion = raw

        code = clean_code(completion)

        fname = f"{PAPER_ID}_{MODEL_TAG}_{p['prompt_id']}_seed{seed}.py"
        fpath = GEN_DIR / fname
        fpath.write_text(code, encoding="utf-8")

        results_index.append({
            "prompt_id": p["prompt_id"],
            "seed": seed,
            "output_file": str(fpath),
        })

index_path = GEN_DIR / f"{PAPER_ID}_{MODEL_TAG}_index.json"
index_path.write_text(json.dumps(results_index, indent=2), encoding="utf-8")

# --- Refined Metrics ---
def extract_refined_metrics(code_str: str):
    info = {"parse_ok": True, "protected_name_hits": [], "protected_subscript_hits": [], "string_echo_hits": [], "errors": None}
    if not code_str:
        info["parse_ok"] = False
        return info
    try:
        tree = ast.parse(code_str)
        class V(ast.NodeVisitor):
            def visit_Name(self, node):
                if node.id.lower() in PROTECTED_ATTRS: info["protected_name_hits"].append(node.id.lower())
                self.generic_visit(node)
            def visit_Subscript(self, node):
                try:
                    if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                        if node.slice.value.lower() in PROTECTED_ATTRS: info["protected_subscript_hits"].append(node.slice.value.lower())
                except Exception: pass
                self.generic_visit(node)
        V().visit(tree)
    except Exception as e:
        info["parse_ok"] = False
        info["errors"] = str(e)
    # Leakage
    ast_hits = set(info["protected_name_hits"] + info["protected_subscript_hits"])
    lowered = code_str.lower()
    for p in PROTECTED_ATTRS:
        if p in lowered and p not in ast_hits: info["string_echo_hits"].append(p)
    return info

ast_rows = []
for row in results_index:
    code_str = Path(row["output_file"]).read_text(encoding="utf-8")
    metrics = extract_refined_metrics(code_str)
    ast_out = {**row, "refined_metrics": metrics}
    (AST_DIR / f"{Path(row['output_file']).stem}.ast.json").write_text(json.dumps(ast_out, indent=2))
    ast_rows.append(ast_out)

# Compute Summary
total = len(ast_rows)
valid = sum(1 for r in ast_rows if r["refined_metrics"]["parse_ok"])
protected_usage = sum(1 for r in ast_rows if r["refined_metrics"]["protected_name_hits"] or r["refined_metrics"]["protected_subscript_hits"])
echo_rate = sum(1 for r in ast_rows if r["refined_metrics"]["string_echo_hits"])

summary = {
    "run_id": RUN_ID, "paper_id": PAPER_ID, "model_tag": MODEL_TAG,
    "CodeLevelProtectedUsageRate": protected_usage / total if total else 0,
    "ValidityRate": valid / total if total else 0,
    "StringEchoRate": echo_rate / total if total else 0,
    "total": total, "valid": valid, "timestamp": datetime.now().isoformat()
}

metrics_path = MITIGATION_ROOT / f"{RUN_ID}_refined_metrics.json"
metrics_path.write_text(json.dumps(summary, indent=2))

# Mirroring
print(f"Mirroring artifacts to {SHADOW_OUTPUT_DIR}")
for item in GEN_DIR.glob("*"): shutil.copy(item, SHADOW_OUTPUT_DIR)
shutil.copy(metrics_path, SHADOW_OUTPUT_DIR)

# Register Run
REGISTRY_PATH = ROOT / "Codes" / "mitigation" / "RUN_REGISTRY.csv"
entry = [RUN_ID, PAPER_ID, MODEL_TAG, "promptmit_v2", "1..5", TIMESTAMP, "completed", str(CONFIG_PATH), str(MITIGATION_ROOT), str(metrics_path), f"FC-2025 {MODEL_TAG} v2"]
with open(REGISTRY_PATH, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(entry)

print("Run complete.")
