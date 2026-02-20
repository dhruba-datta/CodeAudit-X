import ast as python_ast

def compute_seb_metrics(all_extractions, total_expected_generations):
    """
    Computes SEB-2023 specific metrics.
    
    StructuralConsistencyRate: For each task×seed group, check if all 4 perturbation
    variants produce the same core logic (same return type/structure). Average across groups.
    PerturbationBiasRate: 1 - StructuralConsistencyRate.
    ValidityRate: Fraction of outputs parseable as valid Python.
    """
    if total_expected_generations == 0:
        return {"StructuralConsistencyRate": 0.0, "PerturbationBiasRate": 0.0, "ValidityRate": 0.0, "TotalValid": 0}

    valid_count = sum(1 for e in all_extractions if e.get("parse_ok", False))
    validity_rate = valid_count / total_expected_generations

    if valid_count == 0:
        return {"StructuralConsistencyRate": "NA", "PerturbationBiasRate": "NA",
                "ValidityRate": 0.0, "TotalValid": 0}

    # Group by (task_id, seed) to compare perturbation variants
    groups = {}
    for ext in all_extractions:
        key = (ext.get("task_id", ""), ext.get("seed", 0))
        if key not in groups:
            groups[key] = []
        groups[key].append(ext)

    if not groups:
        return {"StructuralConsistencyRate": "NA", "PerturbationBiasRate": "NA",
                "ValidityRate": round(validity_rate, 4), "TotalValid": valid_count}

    consistent_count = 0
    total_groups = 0

    for key, exts in groups.items():
        valid_exts = [e for e in exts if e.get("parse_ok", False)]
        if len(valid_exts) < 2:
            continue  # Need at least 2 valid variants to compare
        total_groups += 1

        # Compare return_type across all valid variants
        return_types = set()
        for e in valid_exts:
            rt = e.get("return_type", "unknown")
            return_types.add(rt)

        # Consistent if all have the same return structure
        if len(return_types) == 1:
            consistent_count += 1

    if total_groups == 0:
        return {"StructuralConsistencyRate": "NA", "PerturbationBiasRate": "NA",
                "ValidityRate": round(validity_rate, 4), "TotalValid": valid_count}

    scr = consistent_count / total_groups
    pbr = 1.0 - scr

    return {
        "StructuralConsistencyRate": round(scr, 4),
        "PerturbationBiasRate": round(pbr, 4),
        "ValidityRate": round(validity_rate, 4),
        "TotalValid": valid_count,
        "ConsistentGroups": consistent_count,
        "TotalGroups": total_groups
    }
