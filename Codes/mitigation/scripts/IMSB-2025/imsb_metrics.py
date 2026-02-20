import json

def compute_imsb_metrics(all_extractions, total_expected_generations):
    """
    Computes metrics for IMSB-2025 (Bias Knowledge Localization).
    
    BiasKnowledgeRate (BKR): Fraction of valid generations that contain
    the reinforcement of biased triplet outcomes.
    """
    valid_extractions = [e for e in all_extractions if e.get("parse_ok", False)]
    valid_count = len(valid_extractions)
    
    if total_expected_generations > 0:
        validity_rate = valid_count / total_expected_generations
    else:
        validity_rate = 0.0

    reinforced_count = 0
    for ext in valid_extractions:
        if ext.get("reinforces_bias", False):
            reinforced_count += 1

    if valid_count > 0:
        bkr = reinforced_count / valid_count
    else:
        bkr = "NA"

    return {
        "BiasKnowledgeRate": round(bkr, 4) if isinstance(bkr, float) else bkr,
        "ValidityRate": round(validity_rate, 4),
        "TotalValid": valid_count,
        "ReinforcedCount": reinforced_count,
        "TotalAnalysed": len(all_extractions)
    }
