def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    suitable = False

    if obj.income >= 70000 and obj.credit_score >= 700:
        suitable = True

    return suitable
