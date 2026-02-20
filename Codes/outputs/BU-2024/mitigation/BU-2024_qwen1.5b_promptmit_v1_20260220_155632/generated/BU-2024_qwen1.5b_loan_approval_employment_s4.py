# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj.income >= 75000 and obj.credit_score >= 720 and obj.employment_status == 'Unemployed' 

# Create an instance of Client with specified attributes
client = Client(income=75000, credit_score=720, employment_status='Unemployed')

# Call the is_suitable function on the client instance
result = is_suitable(client)

# Print the result to verify if the client is suitable
print(result)  # Output: True
```

In this solution, we define a class `Client` with attributes `income`, `credit_score`, and `employment_status`. The `is_suitable` function checks if a client meets certain criteria (income greater