# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     if obj.skills == 'clean' and obj.income <= 50000:
         return True
     else:
         return False

# This function is used to filter the suitable candidates based on the provided criteria.
def filter_candidates(candidates):
    suitable_candidates = []
    for candidate in candidates:
        if is_suitable(candidate):
            suitable_candidates.append(candidate)
    return suitable_candidates

# Test the function
candidates = [Candidate(skills='clean', income=25000), Candidate(skills='clean',