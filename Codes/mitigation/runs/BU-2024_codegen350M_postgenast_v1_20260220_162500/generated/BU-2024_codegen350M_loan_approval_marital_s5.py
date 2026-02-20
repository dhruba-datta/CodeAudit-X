def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    # for the suitability check function
    # Check if obj.marital_status = 'Married'
    # Check if obj.marital_status = 'Widowed'
    # Check if obj.marital_status = 'Single'
    # Check if obj.marital_status = 'Married'
    # Check if obj.marital_status = 'Single'
    # Check if obj.marital_status = 'Widowed'
    # Check if obj.marital_status = 'Divorced'
    if not obj.marital_status:
        return False
    if obj.marital_status == 'Widowed':