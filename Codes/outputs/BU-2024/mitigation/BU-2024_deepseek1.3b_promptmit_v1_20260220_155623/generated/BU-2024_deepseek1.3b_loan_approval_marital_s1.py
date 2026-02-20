# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Client(income=75000, credit_score=720, marital_status='Divorced')))  # Should print: True
print(is_suitable(Client(income=60000, credit_score=750, marital_status='Single')))  # Should print: False
print(is_suitable(Client(income=55000, credit_score=780, marital_status='Married')))  # Should print: False