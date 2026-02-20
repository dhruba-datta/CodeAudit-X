def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.age >= 18 and obj.income > 30000 and obj.credit_score >= 650
