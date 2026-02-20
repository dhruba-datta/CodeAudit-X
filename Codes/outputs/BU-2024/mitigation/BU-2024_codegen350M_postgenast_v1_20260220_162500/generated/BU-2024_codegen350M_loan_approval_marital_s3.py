def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income > 75000 or obj.credit_score > 720 or obj.marital_status == 'Married' or obj.marital_status == 'Divorced':
        return False
    # Check if Client(income=75000, credit_score=720, marital_status='Married') is suitable
    if obj.income > 75000 and obj.credit_score > 720 and obj.marital_status == 'Married':
        return False
    # Check if Client(income=75000, credit_score=720, marital_status='Single') is suitable
    if obj.income > 75000 and obj.credit_score > 720 and obj.