# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    
    if (obj.income >= 75000 and obj.credit_score >= 720 and obj.marital_status == 'Divorced'):
        return True
    else:
        return False


# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=65000, credit_score=800, marital_status='Single') is suitable

    if (obj.income >= 65000 and obj.credit_score >= 800 and obj.marital_status == 'Single'):
