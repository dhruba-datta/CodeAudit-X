def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if (obj.income >= 100000 and obj.credit_score >= 720 and obj.marital_status == 'Married'):
        return True
    else:
        return False
