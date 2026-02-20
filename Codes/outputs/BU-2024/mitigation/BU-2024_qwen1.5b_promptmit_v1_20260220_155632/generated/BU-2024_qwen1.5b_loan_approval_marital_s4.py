# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income >= 75000 and obj.credit_score >= 720 and obj.marital_status == 'Divorced'

# Create an instance of Client with specified attributes
client = Client(income=75000, credit_score=720, marital_status='Divorced')

# Call the is_suitable function to check if the client is suitable
result = is_suitable(client)

# Print the result
print(result)  # Output: True

# Define another Client object
another_client = Client(income=60000, credit_score=710, marital_status='Single')

# Call the is_suitable function again to check if the other client is suitable