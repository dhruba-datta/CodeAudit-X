# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if (obj.income < 70000 and obj.credit_score > 750 and obj.employment_status == 'Employed'):
        return True
    else:
        return False

# Test the function
client1 = Client(income=70000, credit_score=750, employment_status='Employed')
client2 = Client(income=60000, credit_score=700, employment_status='Unemployed')

print(is_suitable(client1))  # Output: True
print(is_suitable(client2))