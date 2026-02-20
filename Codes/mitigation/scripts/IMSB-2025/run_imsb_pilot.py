import torch, json, os, time
from datetime import datetime
from transformers import pipeline, set_seed
from extract_ast import extract_imsb_ast
from imsb_metrics import compute_imsb_metrics

def run_imsb_mitigation(model_tag, version):
    print(f"Starting IMSB-2025 mitigation run: {model_tag} {version}")
    
    config_path = f"Codes/mitigation/configs/IMSB-2025/imsb_prompt_{model_tag}_{version}.json"
    if not os.path.exists(config_path):
        print(f"Config not found: {config_path}")
        return

    with open(config_path, "r") as f:
        config = json.load(f)

    model_name_map = {
        "codegen350M": "Salesforce/codegen-350M-mono",
        "qwen1.5b": "Qwen/Qwen2.5-Coder-1.5B-Instruct",
        "deepseek1.3b": "deepseek-ai/deepseek-coder-1.3b-instruct"
    }
    model_name = model_name_map[model_tag]
    
    print(f"Loading model: {model_name} on mps")
    generator = pipeline("text-generation", model=model_name, device="mps", torch_dtype=torch.float16)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_id = f"IMSB-2025_{model_tag}_promptmit_{version}_{timestamp}"
    run_dir = f"Codes/mitigation/runs/{run_id}"
    gen_dir = os.path.join(run_dir, "generated")
    ast_dir = os.path.join(run_dir, "ast_extract")
    os.makedirs(gen_dir, exist_ok=True)
    os.makedirs(ast_dir, exist_ok=True)

    all_extractions = []
    total_expected = len(config["tasks"]) * len(config["seeds"])

    for task in config["tasks"]:
        for seed in config["seeds"]:
            set_seed(seed)
            out = generator(task["prompt"], max_new_tokens=100, temperature=0.5, do_sample=True, pad_token_id=50256)
            gen_text = out[0]["generated_text"]
            
            # Save generated
            filename = f"IMSB-2025_{model_tag}_{task['id']}_s{seed}.py"
            with open(os.path.join(gen_dir, filename), "w") as f:
                f.write(gen_text)
            
            # Extract AST / Reinforcement
            ext = extract_imsb_ast(gen_text, task["target_object"])
            ext["task_id"] = task["id"]
            ext["seed"] = seed
            ext["file_id"] = filename
            
            with open(os.path.join(ast_dir, filename.replace(".py", ".json")), "w") as f:
                json.dump(ext, f, indent=2)
            
            all_extractions.append(ext)

    metrics = compute_imsb_metrics(all_extractions, total_expected)
    metrics_file = os.path.join(run_dir, f"{run_id}_refined_metrics.json")
    with open(metrics_file, "w") as f:
        json.dump(metrics, f, indent=2)
    
    # Mirror output
    mirror_dir = f"Codes/outputs/IMSB-2025/mitigation/{run_id}"
    os.makedirs(mirror_dir, exist_ok=True)
    os.system(f"cp -r {run_dir}/* {mirror_dir}/")
    
    print(f"Run complete. Metrics: {metrics}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python run_imsb_pilot.py <model_tag> <version>")
    else:
        run_imsb_mitigation(sys.argv[1], sys.argv[2])
