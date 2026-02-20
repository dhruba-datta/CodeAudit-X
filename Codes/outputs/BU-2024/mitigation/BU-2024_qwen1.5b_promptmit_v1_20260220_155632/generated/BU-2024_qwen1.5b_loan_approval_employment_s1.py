# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj.income > 50000 and obj.credit_score >= 680 and obj.employment_status == 'Employed'

# Create an instance of Client with income=75000, credit_score=720, employment_status='Unemployed'
client = Client(income=75000, credit_score=720, employment_status='Unemployed')

# Call the is_suitable function with the client object as an argument
result = is_suitable(client)

# Print the result
print(result)  # Output: False
```

In this solution, we define a `Client` class with attributes for income, credit score, and employment status. We then implement the `is