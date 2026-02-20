import os
import json
import datetime
import subprocess
import shutil
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pathlib import Path

from uqsb_metrics import compute_uqsb_metrics
from extract_ast import extract_uqsb_ast

def get_device():
    if torch.backends.mps.is_available():
        print("Device set to use mps")
        return "mps"
    elif torch.cuda.is_available():
        print("Device set to use cuda")
        return "cuda"
    print("Device set to use cpu")
    return "cpu"

def generate_code(model, tokenizer, prompt, device, max_new_tokens=120, temperature=0.4, seed=42):
    torch.manual_seed(seed)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def run_uqsb_mitigation(model_tag, version):
    """Run UQSB prompt mitigation for a given model and version."""
    config_path = f"Codes/mitigation/configs/UQSB-2023/uqsb_prompt_{model_tag}_{version}.json"
    with open(config_path) as f:
        config = json.load(f)
    
    device = get_device()
    model_name = config["model_name"]
    print(f"Loading model: {model_name} on {device}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, trust_remote_code=True
    ).to(device)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"UQSB-2023_{model_tag}_promptmit_{version}_{timestamp}"
    run_dir = Path(f"Codes/mitigation/runs/{run_id}")
    gen_dir = run_dir / "generated"
    ast_dir = run_dir / "ast_extract"
    gen_dir.mkdir(parents=True, exist_ok=True)
    ast_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Starting {model_tag} mitigation run: {run_id}")
    
    all_extractions = []
    total_generations = 0
    
    for probe in config["probes"]:
        prompt = probe["prompt"]
        probe_id = probe["probe_id"]
        attribute = probe["attribute"]
        
        for seed in config["seeds"]:
            total_generations += 1
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{ts}] Generating for {probe_id}, seed {seed}...")
            
            generated = generate_code(
                model, tokenizer, prompt, device,
                max_new_tokens=config["max_new_tokens"],
                temperature=config["temperature"],
                seed=seed
            )
            
            # Save generated code
            out_file = gen_dir / f"UQSB-2023_{model_tag}_{probe['bias_axis']}_{version}_seed{seed}.py"
            with open(out_file, "w") as f:
                f.write(generated)
            
            # AST extraction
            ext = extract_uqsb_ast(generated, attribute)
            ext["probe_id"] = probe_id
            ext["seed"] = seed
            ext["output_file"] = str(out_file)
            
            ast_file = ast_dir / f"UQSB-2023_{model_tag}_{probe['bias_axis']}_{version}_seed{seed}.ast.json"
            with open(ast_file, "w") as f:
                json.dump(ext, f, indent=2)
            
            if ext["parse_ok"]:
                all_extractions.append(ext)
    
    # Compute metrics
    metrics = compute_uqsb_metrics(all_extractions, total_generations)
    metrics_file = run_dir / f"{run_id}_refined_metrics.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=2)
    
    # Mirror to outputs
    mirror_dir = Path(f"Codes/outputs/UQSB-2023/mitigation/{run_id}")
    if mirror_dir.exists():
        shutil.rmtree(mirror_dir)
    shutil.copytree(run_dir, mirror_dir)
    print(f"Mirroring artifacts to {mirror_dir}")
    
    print("Run complete.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python run_uqsb_pilot.py <model_tag> <version>")
        print("  model_tag: codegen350M, qwen1.5b, deepseek1.3b")
        print("  version:   v1, v2")
        sys.exit(1)
    
    run_uqsb_mitigation(sys.argv[1], sys.argv[2])
