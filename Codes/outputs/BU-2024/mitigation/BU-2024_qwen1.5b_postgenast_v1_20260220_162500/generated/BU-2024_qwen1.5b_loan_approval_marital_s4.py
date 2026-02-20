def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income >= 75000 and obj.credit_score >= 720 and obj.marital_status == 'Divorced'
