import os
import shutil

malformed_id = "FC-2025 | FairCoder: Evaluating Social Bias of LLMs in Code Generation_qwen1.5b_postgenast_v1_20260220_103018"
correct_id = "FC-2025_qwen1.5b_postgenast_v1_20260220_103018"

# 1. Rename folders in mitigation runs
mitigation_run_dir = f"Codes/mitigation/runs/{malformed_id}"
correct_mitigation_run_dir = f"Codes/mitigation/runs/{correct_id}"

if os.path.exists(mitigation_run_dir):
    os.rename(mitigation_run_dir, correct_mitigation_run_dir)
    # rename files inside
    for f in os.listdir(correct_mitigation_run_dir):
        if malformed_id in f:
            new_f = f.replace(malformed_id, correct_id)
            os.rename(os.path.join(correct_mitigation_run_dir, f), os.path.join(correct_mitigation_run_dir, new_f))

# 2. Rename folders in outputs
outputs_bad_dir = "Codes/outputs/FC-2025 | FairCoder: Evaluating Social Bias of LLMs in Code Generation/mitigation/" + malformed_id
outputs_good_dir = "Codes/outputs/FC-2025/mitigation/" + correct_id

if os.path.exists(outputs_bad_dir):
    os.makedirs("Codes/outputs/FC-2025/mitigation", exist_ok=True)
    os.rename(outputs_bad_dir, outputs_good_dir)
    # rename files inside
    for f in os.listdir(outputs_good_dir):
        if malformed_id in f:
            new_f = f.replace(malformed_id, correct_id)
            os.rename(os.path.join(outputs_good_dir, f), os.path.join(outputs_good_dir, new_f))

    # clean up the bad parent dir if empty
    bad_parent = "Codes/outputs/FC-2025 | FairCoder: Evaluating Social Bias of LLMs in Code Generation"
    if os.path.exists(os.path.join(bad_parent, "mitigation")) and not os.listdir(os.path.join(bad_parent, "mitigation")):
        os.rmdir(os.path.join(bad_parent, "mitigation"))
    if os.path.exists(bad_parent) and not os.listdir(bad_parent):
        os.rmdir(bad_parent)

# 3. Update RUN_REGISTRY.csv
with open("Codes/mitigation/RUN_REGISTRY.csv", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if malformed_id in line:
        lines[i] = line.replace(malformed_id, correct_id)
        # Also fix the paper title if it slipped into paper_id column for that row
        lines[i] = lines[i].replace("FC-2025 | FairCoder: Evaluating Social Bias of LLMs in Code Generation,qwen", "FC-2025,qwen")

with open("Codes/mitigation/RUN_REGISTRY.csv", "w") as f:
    f.writelines(lines)

print("Renaming and registry update complete.")
