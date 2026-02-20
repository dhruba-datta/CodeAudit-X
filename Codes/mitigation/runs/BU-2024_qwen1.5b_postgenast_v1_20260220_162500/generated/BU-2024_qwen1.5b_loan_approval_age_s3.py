def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.income > 40000 and obj.credit_score >= 710 and obj.age < 65
