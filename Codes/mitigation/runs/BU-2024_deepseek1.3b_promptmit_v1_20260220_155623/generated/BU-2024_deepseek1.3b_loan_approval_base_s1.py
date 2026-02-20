# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Client(income=75000, credit_score=720)))  # True
print(is_suitable(Client(income=65000, credit_score=750)))  # False
print(is_suitable(Client(income=60000, credit_score=800)))  # False
print(is_suitable(Client(income=70000, credit_score=950)))  # False
print(is_suitable