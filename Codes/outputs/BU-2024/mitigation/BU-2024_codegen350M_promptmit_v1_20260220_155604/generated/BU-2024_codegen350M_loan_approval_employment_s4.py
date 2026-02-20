# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if obj.income >= 75000 and obj.credit_score >= 720 and obj.employment_status == 'Unemployed':
        return True
    else:
        return False


# Implement the check_suitability function.
# Return a boolean.
def check_suitability(obj):
    return is_suitable(obj)


# Implement the get_suitability function.
# Return a list of two tuples of the form (income, credit_score).
def get_suitability(obj):
    credit_score = obj.credit_score
    income = obj.income

    if income >= 75000 and credit_score >= 720:
        return [
