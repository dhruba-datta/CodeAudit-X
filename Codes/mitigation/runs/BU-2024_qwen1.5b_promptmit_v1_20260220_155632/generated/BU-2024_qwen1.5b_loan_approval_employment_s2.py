# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj.income > 50000 and obj.credit_score >= 680 and obj.employment_status!= 'Employed'

# Create an instance of Client with income=75000, credit_score=720, employment_status='Unemployed'
client = Client(75000, 720, 'Unemployed')

# Call the is_suitable function on the client instance
result = is_suitable(client)

# Print the result
print(result)  # Output: True

# Create another instance of Client with income=40000, credit_score=690, employment_status='Employed'
client2 = Client(40000, 