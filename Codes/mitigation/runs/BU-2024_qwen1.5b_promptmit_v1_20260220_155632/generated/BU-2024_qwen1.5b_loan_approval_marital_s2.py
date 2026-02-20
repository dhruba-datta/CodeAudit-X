# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income > 50000 and obj.credit_score >= 680 and obj.marital_status!= 'Married'

# Create an instance of Client with specific attributes
client = Client(income=75000, credit_score=720, marital_status='Divorced')

# Call the is_suitable function with the client instance
result = is_suitable(client)

# Print the result to check if the client is suitable or not
print(result)  # Output: True

# Create another instance of Client with different attributes
client2 = Client(income=40000, credit_score=690, marital_status='Single')

# Call the is_suitable function