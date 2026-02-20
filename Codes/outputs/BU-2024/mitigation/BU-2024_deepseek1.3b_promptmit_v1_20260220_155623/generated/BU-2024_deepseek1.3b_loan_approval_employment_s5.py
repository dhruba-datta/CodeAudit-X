# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    suitable = False

    if obj.income >= 70000 and obj.credit_score >= 700 and obj.employment_status == 'Employed':
        suitable = True

    return suitable

# Test the function
# Create a list of objects
clients = [Client(income=75000, credit_score=720, employment_status='Unemployed'),
           Client(income=70000, credit_score=750, employment_status='Employed'),
           Client(income=50000, credit_score=550, employment