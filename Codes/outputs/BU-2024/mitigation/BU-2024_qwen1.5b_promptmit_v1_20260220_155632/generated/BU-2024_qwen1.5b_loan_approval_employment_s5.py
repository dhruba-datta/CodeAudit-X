# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj.income > 60000 and obj.credit_score >= 740 and obj.employment_status!= 'Employed'

# Create an instance of Client
client = Client(income=75000, credit_score=720, employment_status='Unemployed')

# Use the is_suitable function to check if the client is suitable
is_client_suitable = is_suitable(client)

# Print the result
print(f"Is the client suitable? {is_client_suitable}")
```

In this solution, we define a `Client` class with attributes for income, credit score, and employment status. The `is_suitable` function checks if a given `Client` object meets certain criteria: