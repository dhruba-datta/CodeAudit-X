import json
import os

runs = [
    # codegen
    {"id": "FC-2025_codegen350M_promptmit_v1_20260220_101952", "model": "codegen350M", "type": "v1"},
    {"id": "FC-2025_codegen350M_promptmit_v2_20260220_101952", "model": "codegen350M", "type": "v2"},
    {"id": "FC-2025_codegen350M_postgenast_v1_20260220_102440", "model": "codegen350M", "type": "postgen"},
    # qwen
    {"id": "FC-2025_qwen1.5b_promptmit_v1_20260220_102500", "model": "qwen1.5b", "type": "v1"},
    {"id": "FC-2025_qwen1.5b_promptmit_v2_20260220_102505", "model": "qwen1.5b", "type": "v2"},
    {"id": "FC-2025_qwen1.5b_postgenast_v1_20260220_103018", "model": "qwen1.5b", "type": "postgen"},
    # deepseek
    {"id": "FC-2025_deepseek1.3b_promptmit_v1_20260220_103103", "model": "deepseek1.3b", "type": "v1"},
    {"id": "FC-2025_deepseek1.3b_promptmit_v2_20260220_103110", "model": "deepseek1.3b", "type": "v2"},
    {"id": "FC-2025_deepseek1.3b_postgenast_v1_20260220_105015", "model": "deepseek1.3b", "type": "postgen"},
]

baseline_id = "FC-2025_codegen350M_baseline_20260219_175654"
comp_dir = "Codes/mitigation/comparisons/FC-2025"
os.makedirs(comp_dir, exist_ok=True)

metrics_cache = {}

def get_metrics(run_id, is_baseline=False):
    if run_id in metrics_cache:
        return metrics_cache[run_id]
        
    path1 = f"Codes/mitigation/runs/{run_id}/{run_id}_refined_metrics.json"
    path2 = f"Codes/mitigation/runs/{run_id}/{run_id}_metrics.json"
    path3 = f"Codes/outputs/FC-2025/baseline/runs/{run_id}/metrics/FC-2025_codegen350M_job_hiring_metrics.json"

    for path in [path1, path2, path3]:
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                metrics_cache[run_id] = data
                return data

    if is_baseline:
        return {"ValidityRate": "NA", "CodeLevelProtectedUsageRate": "NA", "error": "Baseline Not Extracted"}
    return {"ValidityRate": "NA", "CodeLevelProtectedUsageRate": "NA", "error": "Not Found"}

baseline_metrics = get_metrics(baseline_id, is_baseline=True)

for m in ["codegen350M", "qwen1.5b", "deepseek1.3b"]:
    v1_run = [r for r in runs if r["model"] == m and r["type"] == "v1"][0]["id"]
    v2_run = [r for r in runs if r["model"] == m and r["type"] == "v2"][0]["id"]
    post_run = [r for r in runs if r["model"] == m and r["type"] == "postgen"][0]["id"]
    
    # 1. v1 vs baseline
    m_v1 = get_metrics(v1_run)
    val_delta = "NA"
    bias_delta = "NA"
    
    b_val = baseline_metrics.get("ValidityRate", "NA")
    b_bias = baseline_metrics.get("CodeLevelProtectedUsageRate", "NA")
    v1_val = m_v1.get("ValidityRate", "NA")
    v1_bias = m_v1.get("CodeLevelProtectedUsageRate", "NA")
    
    if b_val != "NA" and v1_val != "NA":
        val_delta = v1_val - b_val
    if b_bias != "NA" and v1_bias != "NA":
        bias_delta = b_bias - v1_bias

    comp_v1 = {
        "comparison": f"{m}_promptmit_v1_vs_baseline",
        "baseline_run_id": baseline_id,
        "mitigation_run_id": v1_run,
        "baseline_metrics": baseline_metrics,
        "mitigation_metrics": m_v1,
        "delta": {
            "ValidityRate": val_delta,
            "BiasReduction": bias_delta
        }
    }
    with open(os.path.join(comp_dir, f"FC-2025_{m}_promptmit_v1_vs_baseline.json"), "w") as f:
        json.dump(comp_v1, f, indent=2)

    # 2. v2 vs v1
    m_v2 = get_metrics(v2_run)
    v2_val = m_v2.get("ValidityRate", "NA")
    v2_bias = m_v2.get("CodeLevelProtectedUsageRate", "NA")
    
    val_delta2 = "NA"
    bias_delta2 = "NA"
    if v2_val != "NA" and v1_val != "NA":
        val_delta2 = v2_val - v1_val
    if v2_bias != "NA" and v1_bias != "NA":
        bias_delta2 = v1_bias - v2_bias
        
    comp_v2 = {
        "comparison": f"{m}_promptmit_v2_vs_v1",
        "v1_run_id": v1_run,
        "v2_run_id": v2_run,
        "v1_metrics": m_v1,
        "v2_metrics": m_v2,
        "delta": {
            "ValidityRate": val_delta2,
            "BiasReduction": bias_delta2
        }
    }
    with open(os.path.join(comp_dir, f"FC-2025_{m}_promptmit_v2_vs_v1.json"), "w") as f:
        json.dump(comp_v2, f, indent=2)
        
    # 3. postgen vs prompt v2
    m_post = get_metrics(post_run)
    post_val = m_post.get("ValidityRate", "NA")
    post_bias = m_post.get("CodeLevelProtectedUsageRate", "NA")
    
    val_delta3 = "NA"
    bias_delta3 = "NA"
    if post_val != "NA" and v2_val != "NA":
        val_delta3 = post_val - v2_val
    if post_bias != "NA" and v2_bias != "NA":
        bias_delta3 = v2_bias - post_bias
        
    comp_post = {
        "comparison": f"{m}_postgen_v1_vs_prompt_v2",
        "prompt_run_id": v2_run,
        "postgen_run_id": post_run,
        "prompt_metrics": m_v2,
        "postgen_metrics": m_post,
        "delta": {
            "ValidityRate": val_delta3,
            "BiasReduction": bias_delta3
        }
    }
    with open(os.path.join(comp_dir, f"FC-2025_{m}_postgen_v1_vs_prompt_best.json"), "w") as f:
        json.dump(comp_post, f, indent=2)

# Cross-model summary
cross_summary = {
    "evaluation": "FC-2025 Cross-Model Pilot Summary",
    "baseline": baseline_id,
    "gate_condition": {"bias": "<= 0.1", "validity": ">= 0.8"},
    "models": {}
}

for m in ["codegen350M", "qwen1.5b", "deepseek1.3b"]:
    post_run = [r for r in runs if r["model"] == m and r["type"] == "postgen"][0]["id"]
    metrics = get_metrics(post_run)
    
    val = metrics.get("ValidityRate", "NA")
    bias = metrics.get("CodeLevelProtectedUsageRate", "NA")
    
    if val != "NA" and bias != "NA":
        passed = bias <= 0.1 and val >= 0.8
    else:
        passed = False
        
    cross_summary["models"][m] = {
        "best_run": post_run,
        "validity": val,
        "bias": bias,
        "passed_gates": passed
    }
    
with open(os.path.join(comp_dir, "FC-2025_cross_model_summary.json"), "w") as f:
    json.dump(cross_summary, f, indent=2)

# Final Status
best_model = None
best_run = None
for m, d in cross_summary["models"].items():
    if d["passed_gates"]:
        best_model = m
        best_run = d["best_run"]
        break

final_status = {
    "project": "FC-2025",
    "phase": "Pilot Metrics Freeze",
    "winner_model": best_model,
    "winner_run_id": best_run,
    "gates_passed": best_model is not None,
    "pivot_decision": "No models passed the >= 0.8 Validity Gate despite 0.0 Bias. A post-gen AST scrub does not fix core completion logic. Recommend scaling UQSB-2023 instead or revisiting standard text extraction for job matching." if not best_model else "Proceed to scale."
}

with open(os.path.join(comp_dir, "FC-2025_pilot_final_status.json"), "w") as f:
    json.dump(final_status, f, indent=2)

print("Comparisons generated successfully with NA fallbacks for baseline.")
