import os, json, datetime, shutil
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from seb_metrics import compute_seb_metrics
from extract_ast import extract_seb_ast

def get_device():
    if torch.backends.mps.is_available(): return "mps"
    elif torch.cuda.is_available(): return "cuda"
    return "cpu"

def generate_code(model, tokenizer, prompt, device, max_new_tokens=100, temperature=0.2, seed=42):
    torch.manual_seed(seed)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=max_new_tokens,
            temperature=temperature, do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def run_seb_mitigation(model_tag, version):
    config_path = f"Codes/mitigation/configs/SEB-2023/seb_prompt_{model_tag}_{version}.json"
    with open(config_path) as f:
        config = json.load(f)

    device = get_device()
    model_name = config["model_name"]
    print(f"Loading model: {model_name} on {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model_obj = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16, trust_remote_code=True
    ).to(device)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"SEB-2023_{model_tag}_promptmit_{version}_{timestamp}"
    run_dir = Path(f"Codes/mitigation/runs/{run_id}")
    gen_dir = run_dir / "generated"
    ast_dir = run_dir / "ast_extract"
    gen_dir.mkdir(parents=True, exist_ok=True)
    ast_dir.mkdir(parents=True, exist_ok=True)

    print(f"Starting {model_tag} mitigation run: {run_id}")

    all_extractions = []
    total_generations = 0

    for task in config["tasks"]:
        task_id = task["task_id"]
        for pert in task["perturbations"]:
            variant_id = pert["variant_id"]
            prompt = pert["prompt"]
            for seed in config["seeds"]:
                total_generations += 1
                ts = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[{ts}] {task_id}/{variant_id}, seed {seed}...")

                generated = generate_code(
                    model_obj, tokenizer, prompt, device,
                    max_new_tokens=config["max_new_tokens"],
                    temperature=config["temperature"], seed=seed
                )

                out_file = gen_dir / f"SEB-2023_{model_tag}_{task_id}_{variant_id}_{version}_seed{seed}.py"
                with open(out_file, "w") as f:
                    f.write(generated)

                ext = extract_seb_ast(generated)
                ext["task_id"] = task_id
                ext["variant_id"] = variant_id
                ext["seed"] = seed
                ext["output_file"] = str(out_file)

                ast_file = ast_dir / f"SEB-2023_{model_tag}_{task_id}_{variant_id}_{version}_seed{seed}.ast.json"
                with open(ast_file, "w") as f:
                    json.dump(ext, f, indent=2)

                all_extractions.append(ext)

    metrics = compute_seb_metrics(all_extractions, total_generations)
    metrics_file = run_dir / f"{run_id}_refined_metrics.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=2)

    mirror_dir = Path(f"Codes/outputs/SEB-2023/mitigation/{run_id}")
    if mirror_dir.exists(): shutil.rmtree(mirror_dir)
    shutil.copytree(run_dir, mirror_dir)
    print(f"Mirroring to {mirror_dir}")
    print("Run complete.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python run_seb_pilot.py <model_tag> <version>")
        sys.exit(1)
    run_seb_mitigation(sys.argv[1], sys.argv[2])
