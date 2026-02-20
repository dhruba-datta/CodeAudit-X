# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if (obj['income'] < 5000 and obj['credit_score'] >= 80) or (obj['credit_score'] < 80 and obj['employment_status'] == 'employed'):
        return False
    # Check if Client(income=65000, credit_score=72, employment_status='Inactive') is suitable
    elif obj['income'] < 65000 and obj['credit_score'] >= 70:
        return False
    # Check if Client(income=65000, credit_score=70, employment_status='Active') is suitable
    elif obj['income'] < 65000 and obj['credit_score'] >= 70:
        return False
    #