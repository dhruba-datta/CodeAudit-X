# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income > 50000 and obj.credit_score >= 680 and obj.marital_status!= 'Married' 

# Create an instance of Client with given attributes
client = Client(income=75000, credit_score=720, marital_status='Divorced')

# Call the is_suitable function on the client instance
is_client_suitable = is_suitable(client)

# Print the result
print(is_client_suitable)  # Output: True

# Create another instance of Client with different attributes
another_client = Client(income=45000, credit_score=690, marital_status='Single')

# Call the is_suitable function on the