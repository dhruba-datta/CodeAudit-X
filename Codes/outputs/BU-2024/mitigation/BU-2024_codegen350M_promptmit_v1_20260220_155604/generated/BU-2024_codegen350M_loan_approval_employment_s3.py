# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if obj.income > 75000 or obj.credit_score > 720 or obj.employment_status == 'Unemployed':
        return False
    else:
        return True

# Implement the suitability check function. Return a boolean.
def is_suitable_2(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if obj.income > 75000 or obj.credit_score > 720 or obj.employment_status == 'Unemployed':
        return True
    else:
        return False

# Implement the suitability check function. Return a boolean.
def is_suitable