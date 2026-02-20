def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.age < 24 or obj.age > 65:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is not suitable
    elif obj.age < 18 or obj.age > 65:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    elif obj.credit_score > 90 or obj.credit_score < 0:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is not suitable
    elif obj.credit_score < 80 or obj.credit