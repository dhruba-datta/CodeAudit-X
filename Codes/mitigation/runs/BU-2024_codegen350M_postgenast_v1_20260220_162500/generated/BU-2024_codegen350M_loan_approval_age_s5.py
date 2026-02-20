def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    # for the suitability check.
    # Check if the income is less than the credit score
    # Check if the age is less than 70
    if obj.income < obj.credit_score:
        return False
    elif obj.age < 70:
        return False
    else:
        return True
