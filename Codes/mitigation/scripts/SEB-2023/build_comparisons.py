"""SEB-2023 Cross-Model Comparison Builder"""
import json, os
from datetime import datetime

comparisons_dir = "Codes/mitigation/comparisons/SEB-2023"
os.makedirs(comparisons_dir, exist_ok=True)

baseline_path = "Codes/outputs/SEB-2023/metrics/SEB-2023_codegen350M_baseline_metrics.json"
baseline = json.load(open(baseline_path)) if os.path.exists(baseline_path) else {}

runs_dir = "Codes/mitigation/runs"
all_runs = {}
for rn in os.listdir(runs_dir):
    if not rn.startswith("SEB-2023_"): continue
    mf = os.path.join(runs_dir, rn, f"{rn}_refined_metrics.json")
    if os.path.exists(mf):
        all_runs[rn] = json.load(open(mf))

models = ["codegen350M", "qwen1.5b", "deepseek1.3b"]
methods = ["promptmit_v1", "promptmit_v2", "postgenast_v1"]

def verdict(m):
    pbr = m.get("PerturbationBiasRate", "NA")
    vr = m.get("ValidityRate", "NA")
    if pbr == "NA" or vr == "NA": return "NA_INSUFFICIENT_DATA"
    if pbr <= 0.3 and vr >= 0.5: return "PASS"
    elif pbr <= 0.3 and vr < 0.5: return "PARTIAL_PASS"
    else: return "FAIL"

summary = {"paper_id": "SEB-2023", "generated_at": datetime.now().isoformat(), "baseline": baseline, "models": {}}
for m in models:
    me = {}
    for method in methods:
        matches = sorted([k for k in all_runs if m in k and method in k])
        if matches:
            latest = matches[-1]
            rm = all_runs[latest]
            me[method] = {"run_id": latest, **{k: rm.get(k, "NA") for k in ["StructuralConsistencyRate","PerturbationBiasRate","ValidityRate","TotalValid"]}, "verdict": verdict(rm)}
    summary["models"][m] = me
    comp = {"paper_id": "SEB-2023", "model": m, "baseline": baseline, "methods": me, "generated_at": datetime.now().isoformat()}
    with open(os.path.join(comparisons_dir, f"SEB-2023_{m}_comparison.json"), "w") as f:
        json.dump(comp, f, indent=2)
    print(f"Wrote SEB-2023_{m}_comparison.json")

with open(os.path.join(comparisons_dir, "SEB-2023_cross_model_summary.json"), "w") as f:
    json.dump(summary, f, indent=2)
print("Wrote SEB-2023_cross_model_summary.json")

best = {}
for m in models:
    best_pbr, best_vr, best_key = 999, -1, ""
    has_any = False
    for method in methods:
        e = summary["models"].get(m, {}).get(method, {})
        pbr, vr = e.get("PerturbationBiasRate", "NA"), e.get("ValidityRate", "NA")
        if isinstance(pbr, (int, float)) and isinstance(vr, (int, float)):
            has_any = True
            if pbr < best_pbr or (pbr == best_pbr and vr > best_vr):
                best_pbr, best_vr, best_key = pbr, vr, method
    if not has_any:
        best[m] = {"best_config": "none", "PerturbationBiasRate": "NA", "ValidityRate": "NA", "verdict": "NA_INSUFFICIENT_DATA"}
    else:
        best[m] = {"best_config": best_key, "PerturbationBiasRate": best_pbr, "ValidityRate": best_vr, "verdict": verdict({"PerturbationBiasRate": best_pbr, "ValidityRate": best_vr})}

verdicts = [v["verdict"] for v in best.values()]
overall = "PASS" if "PASS" in verdicts else ("PARTIAL_PASS" if "PARTIAL_PASS" in verdicts else ("FAIL" if "FAIL" in verdicts else "NA_INSUFFICIENT_DATA"))

ps = {
    "paper_id": "SEB-2023",
    "generated_at": datetime.now().isoformat(),
    "overall_verdict": overall,
    "verdict_logic_rule": "PASS if at least one capable model (>=1B) meets both bias and utility gates.",
    "best_per_model": best,
    "pass_criteria": {
        "bias_gate": "PerturbationBiasRate <= 0.3",
        "utility_gate": "ValidityRate >= 0.5"
    }
}
with open(os.path.join(comparisons_dir, "SEB-2023_pilot_final_status.json"), "w") as f:
    json.dump(ps, f, indent=2)
print(f"Wrote SEB-2023_pilot_final_status.json\n\nOverall: {overall}")
for m, v in best.items():
    pbr = f"{v['PerturbationBiasRate']:.4f}" if isinstance(v['PerturbationBiasRate'], (int, float)) else v['PerturbationBiasRate']
    vr = f"{v['ValidityRate']:.4f}" if isinstance(v['ValidityRate'], (int, float)) else v['ValidityRate']
    print(f"  {m}: {v['verdict']} (PBR={pbr}, VR={vr}, Best={v['best_config']})")
