def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.income > 75000 and obj.credit_score > 720 and obj.age >= 65:
        return True
    else:
        return False
