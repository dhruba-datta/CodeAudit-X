# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if obj.income < 0 or obj.credit_score < 0 or obj.employment_status!= 'Unemployed':
        return False
    return True
