# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj <= 75000:
        return False
    # Check if Client(income=75000, credit_score=720, marital_status='Married') is suitable
    elif obj <= 75000 * 2:
        return False
    # Check if Client(income=75000, credit_score=720, marital_status='Single') is suitable
    elif obj <= 75000 * 3:
        return False
    # Check if Client(income=75000, credit_score=720, marital_status='Single') is suitable
    elif obj <= 75000 * 4:
        return False
    # Check if Client(income=75000, credit_score=