# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Client(income=75000, credit_score=720, employment_status='Unemployed')))
print(is_suitable(Client(income=65000, credit_score=700, employment_status='Employed')))
print(is_suitable(Client(income=50000, credit_score=600, employment_status='Retired')))
print(is_suitable(Client(income=55000