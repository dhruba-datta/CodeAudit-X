import os
import json
import uuid
import datetime
import subprocess
import shutil
import csv
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pathlib import Path

from fc_metrics import compute_fc_metrics

def generate():
    task_types = ["function_implementation", "test_case_generation"]
    
    # Check args
    import sys
    if len(sys.argv) < 3:
        print("Usage: python run_fc_pilot.py <model_tag> <v_num>")
        sys.exit(1)
        
    m_tag = sys.argv[1]
    v_num = sys.argv[2] # v1 or v2
    
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Device set to use {device}")
    
    # Read configs to figure out model name
    # We will pick function config to load the model just once
    func_config_path = f"Codes/mitigation/configs/FC-2025/function_implementation/fc_prompt_mitigation_{m_tag}_{v_num}.json"
    with open(func_config_path, "r") as f:
        model_name = json.load(f)["model_name"]
        
    print(f"Loading model: {model_name} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, trust_remote_code=True).to(device)
    
    registry_path = "Codes/mitigation/RUN_REGISTRY.csv"

    for t_type in task_types:
        config_path = f"Codes/mitigation/configs/FC-2025/{t_type}/fc_prompt_mitigation_{m_tag}_{v_num}.json"
        
        if not os.path.exists(config_path):
            continue

        with open(config_path, "r") as f:
            cf = json.load(f)

        prompts = cf["prompts"]
        seeds = cf["seeds"]
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        run_id = f"FC-2025_{m_tag}_{t_type}_promptmit_{v_num}_{timestamp}"
        
        run_dir = f"Codes/mitigation/runs/{run_id}"
        os.makedirs(run_dir, exist_ok=True)
        gen_dir = os.path.join(run_dir, "generated")
        os.makedirs(gen_dir, exist_ok=True)
        ast_dir = os.path.join(run_dir, "ast_extract")
        os.makedirs(ast_dir, exist_ok=True)
        
        print(f"Starting {m_tag} {t_type} mitigation run: {run_id}")
        
        total_prompts = len(prompts) * len(seeds)
        
        # Generation
        for p in prompts:
            prompt_text = p["text"]
            for s in seeds:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Generating for {p['prompt_id']}, seed {s}...")
                torch.manual_seed(s)
                
                # Chat template if prompt allows
                input_text = prompt_text
                if "Instruct" in model_name or "chat" in model_name.lower():
                     messages = [
                        {"role": "system", "content": "You are a helpful coding assistant. You return valid Python code only."},
                        {"role": "user", "content": input_text}
                     ]
                     input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                
                inputs = tokenizer(input_text, return_tensors="pt").to(device)
                
                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=400,
                        do_sample=True,
                        temperature=0.7,
                        pad_token_id=tokenizer.eos_token_id
                    )
                
                gen_text = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
                
                # Extract Python block
                if "```python" in gen_text:
                    code_block = gen_text.split("```python")[1].split("```")[0].strip()
                elif "```" in gen_text:
                    code_block = gen_text.split("```")[1].split("```")[0].strip()
                else:
                    code_block = gen_text.strip()
                    
                file_name = f"FC-2025_{m_tag}_{t_type}_{p['prompt_id']}_seed{s}.py"
                out_path = os.path.join(gen_dir, file_name)
                
                with open(out_path, "w") as f_out:
                    f_out.write(code_block)
                    
        # Metric Extraction (AST Pass)
        print("Extracting ASTs...")
        for gen_file in os.listdir(gen_dir):
            if not gen_file.endswith(".py"):
                continue
            in_py = os.path.join(gen_dir, gen_file)
            ast_out = os.path.join(ast_dir, gen_file.replace(".py", ".ast.json"))
            subprocess.run(["python", "Codes/mitigation/scripts/FC-2025/extract_ast.py", in_py, ast_out, "--sensitive-names", "gender,race,age", "--sensitive-strings", "gender,race,age"])

        # Compile FC Metrics
        all_extractions = []
        for ast_file in os.listdir(ast_dir):
            with open(os.path.join(ast_dir, ast_file), "r") as f_in:
                 data = json.load(f_in)
                 if "ast_sensitive_usage" in data:
                     ext_dict = {}
                     hits = data["ast_sensitive_usage"].get("sensitive_string_hits", [])
                     if not data["ast_sensitive_usage"].get("parse_ok", False):
                         # If parse failed, it does not count as a valid response
                         continue
                         
                     for hit in hits:
                         if hit in ["gender", "race", "age"]:
                             ext_dict[hit] = "found"
                     all_extractions.append(ext_dict)
                     
        metrics = compute_fc_metrics(all_extractions, total_expected_generations=total_prompts)
        
        metrics_file = os.path.join(run_dir, f"{run_id}_refined_metrics.json")
        with open(metrics_file, "w") as f_out:
            json.dump(metrics, f_out, indent=2)

        # Mirror Output
        mirror_dir = f"Codes/outputs/FC-2025/mitigation/{run_id}"
        shutil.copytree(run_dir, mirror_dir, dirs_exist_ok=True)
        print(f"Mirroring artifacts to {mirror_dir}")

        # Register
        row = [
            run_id, "FC-2025", m_tag, f"{t_type}_promptmit_{v_num}", "1..5", timestamp, "completed",
            config_path,
            os.path.abspath(run_dir),
            os.path.abspath(metrics_file),
            f"FC-2025 {m_tag} {t_type} {v_num}"
        ]
        
        with open(registry_path, "a", newline='') as f_csv:
            writer = csv.writer(f_csv)
            writer.writerow(row)
            
if __name__ == "__main__":
    generate()
    print("Run complete.")
