# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if (obj.income >= 75000 and obj.credit_score >= 720 and obj.employment_status == 'Unemployed'):
        return True
    else:
        return False

# Test the function
client1 = Client(income=75000, credit_score=720, employment_status='Unemployed')
print(is_suitable(client1))

client2 = Client(income=60000, credit_score=750, employment_status='Employed')
print(is_suitable(client2))

client3 =