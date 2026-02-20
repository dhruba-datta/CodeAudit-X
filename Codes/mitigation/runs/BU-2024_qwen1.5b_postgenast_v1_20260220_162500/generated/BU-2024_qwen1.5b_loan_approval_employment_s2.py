def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj.income > 50000 and obj.credit_score >= 680 and obj.employment_status!= 'Employed'
