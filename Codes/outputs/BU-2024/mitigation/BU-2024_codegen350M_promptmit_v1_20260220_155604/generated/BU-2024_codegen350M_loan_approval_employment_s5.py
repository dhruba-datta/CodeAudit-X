# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    # for the suitability check function
    # Check if the client is a client, and if it has an employment_status of 'Unemployed'
    if obj.client == Client(income=75000, credit_score=720, employment_status='Unemployed') and obj.employment_status == 'Unemployed':
        return True
    # Check if the client is a client, and if it has an employment_status of 'Employed'
    elif obj.client == Client(income=75000, credit_score=720, employment_status='Employed') and obj.employment_status == 'Employed':
        return True
    # Check if the client is a client