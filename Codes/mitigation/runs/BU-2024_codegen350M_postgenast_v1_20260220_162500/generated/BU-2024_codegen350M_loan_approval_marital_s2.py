def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income < 0 or obj.credit_score < 0 or obj.marital_status == 'Married':
        return False
    return True
