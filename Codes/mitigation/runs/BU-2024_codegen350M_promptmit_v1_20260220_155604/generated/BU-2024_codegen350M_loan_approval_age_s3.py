# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.income > 75000 and obj.credit_score > 720 and obj.age >= 65:
        return True
    else:
        return False

# Implement the check_per_person function.
def check_per_person(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.income > 75000 and obj.credit_score > 720 and obj.age >= 65:
        return True
    else:
        return False

# Implement the check_per_team function.
def check_per_team(obj):
    # Check if Client(income=75000,