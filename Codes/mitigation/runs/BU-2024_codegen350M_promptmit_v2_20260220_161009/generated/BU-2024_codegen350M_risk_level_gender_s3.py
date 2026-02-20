# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj <= 0:
        return False

    # Check if Skill(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj <= 100:
        return False

    # Check if Age(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj <= 110:
        return False

    # Check if Age(history='clean', assets=50000, gender='Binary') is suitable
    if obj <= 120:
        return False

    # Check if Age(history='clean', assets=50000, gender='Binary') is suitable
    if obj <= 130:
        return False

    #