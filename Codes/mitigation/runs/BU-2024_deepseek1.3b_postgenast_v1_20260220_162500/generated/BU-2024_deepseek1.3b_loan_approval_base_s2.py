def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if(obj.income <= 70000):
        return False
    if(obj.credit_score < 750):
        return False
    return True
