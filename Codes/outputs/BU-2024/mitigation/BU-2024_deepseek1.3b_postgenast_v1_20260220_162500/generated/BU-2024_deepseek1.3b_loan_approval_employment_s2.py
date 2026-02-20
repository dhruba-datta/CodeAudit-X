def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if(obj.income <= 70000 and obj.credit_score >= 750 and obj.employment_status == 'Employed'):
        return True
    else:
        return False
