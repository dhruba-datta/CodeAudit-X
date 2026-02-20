import json, os

configs_dir = "Codes/mitigation/configs/SEB-2023"
os.makedirs(configs_dir, exist_ok=True)

models = [
    {"name": "Salesforce/codegen-350M-mono", "tag": "codegen350M"},
    {"name": "Qwen/Qwen2.5-Coder-1.5B-Instruct", "tag": "qwen1.5b"},
    {"name": "deepseek-ai/deepseek-coder-1.3b-instruct", "tag": "deepseek1.3b"}
]

# 3 tasks × 4 perturbation variants each
TASKS = {
    "check_even": {
        "base": 'def is_even(n):\n    """Check if a number is even."""\n',
        "short": 'def is_even(n):\n',
        "formal": 'Write a Python function to check if an integer is even.\ndef is_even(n):\n',
        "implied": 'def is_even(num):\n    # return true if num is even\n'
    },
    "find_max": {
        "base": 'def find_max(lst):\n    """Find the maximum element in a list."""\n',
        "short": 'def find_max(lst):\n',
        "formal": 'Write a Python function to find the maximum element in a list.\ndef find_max(lst):\n',
        "implied": 'def find_max(numbers):\n    # return the largest number in the list\n'
    },
    "reverse_string": {
        "base": 'def reverse_string(s):\n    """Reverse a string."""\n',
        "short": 'def reverse_string(s):\n',
        "formal": 'Write a Python function to reverse a string.\ndef reverse_string(s):\n',
        "implied": 'def reverse_string(text):\n    # return the string reversed\n'
    }
}

PERTURBATION_IDS = ["base", "short", "formal", "implied"]

def make_v1_prompt(task_id, variant_id):
    """v1 mitigation: Add a standardized instruction preamble for consistency."""
    base_prompt = TASKS[task_id][variant_id]
    preamble = "# Implement the following function. Return the result directly.\n"
    return preamble + base_prompt

def make_v2_prompt(task_id, variant_id):
    """v2 mitigation: Explicit consistency-promoting preamble."""
    base_prompt = TASKS[task_id][variant_id]
    preamble = (
        "# INSTRUCTIONS: Implement the function below using a single return statement.\n"
        "# Use the most concise idiomatic Python approach.\n"
        "# Do not add extra functions or helper code.\n"
    )
    return preamble + base_prompt

for version in ["v1", "v2"]:
    for model in models:
        config = {
            "paper_id": "SEB-2023",
            "model_name": model["name"],
            "model_tag": model["tag"],
            "version": version,
            "domain": "Stability Auditing / Prompt Perturbations",
            "max_new_tokens": 100,
            "temperature": 0.2,
            "do_sample": True,
            "seeds": [1, 2, 3, 4, 5],
            "tasks": []
        }
        for task_id in TASKS:
            task_entry = {"task_id": task_id, "perturbations": []}
            for variant_id in PERTURBATION_IDS:
                if version == "v1":
                    prompt = make_v1_prompt(task_id, variant_id)
                else:
                    prompt = make_v2_prompt(task_id, variant_id)
                task_entry["perturbations"].append({
                    "variant_id": variant_id,
                    "prompt": prompt
                })
            config["tasks"].append(task_entry)

        fname = f"seb_prompt_{model['tag']}_{version}.json"
        with open(os.path.join(configs_dir, fname), "w") as f:
            json.dump(config, f, indent=2)

# Postgen configs
for model in models:
    pc = {
        "paper_id": "SEB-2023",
        "model_tag": model["tag"],
        "source_run_id": f"SEB-2023_{model['tag']}_promptmit_best_PLACEHOLDER",
        "scrub_strategy": "normalize_structure"
    }
    fname = f"seb_postgen_{model['tag']}_v1.json"
    with open(os.path.join(configs_dir, fname), "w") as f:
        json.dump(pc, f, indent=2)

print("Generated SEB-2023 prompt and postgen configs.")
