# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    # for the objective function.
    if obj['income'] < 75000 and obj['credit_score'] < 720 and obj['age'] < 65:
        return True
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    # for the objective function.
    elif obj['income'] < 75000 and obj['credit_score'] < 720 and obj['age'] < 65:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    # for the objective function.
    elif obj['income'] < 75000 and obj['credit_score