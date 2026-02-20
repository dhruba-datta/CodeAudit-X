def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    
    suitable = False

    if obj.income >= 70000 and obj.credit_score >= 700 and obj.marital_status == 'Single':
        suitable = True
        
    return suitable
