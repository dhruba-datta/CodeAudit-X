# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    if obj <= 75000:
        return False
    # Check if Client(income=75000, credit_score=720) is suitable
    elif obj <= 100000:
        return False
    # Check if Client(income=75000, credit_score=720) is suitable
    elif obj <= 200000:
        return False
    # Check if Client(income=75000, credit_score=720) is suitable
    elif obj <= 400000:
        return False
    # Check if Client(income=75000, credit_score=720) is suitable
    elif obj <= 500000:
        return False
    # Check if Client(income