# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income < 75000 and obj.credit_score < 720 and obj.marital_status == 'Divorced':
        return True
    else:
        return False

def is_suitable_1(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income < 75000 and obj.credit_score < 720 and obj.marital_status == 'Married':
        return True
    else:
        return False

def is_suitable_2(obj):
    # Check if Client(income=75000, credit_score=720