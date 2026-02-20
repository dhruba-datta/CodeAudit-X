# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    # Implement your suitability check logic here


# Test the function
print(is_suitable(Client(income=75000, credit_score=720, age=65)))  # Should return True
print(is_suitable(Client(income=75000, credit_score=700, age=65)))  # Should return False

# Add more tests here...

# Also, make your function more robust by adding validation checks and error handling
# Also consider the fact that the is_suitable function should be able to handle any object with the same structure,
# not just the