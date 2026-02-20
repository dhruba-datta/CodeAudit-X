# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income > 50000 and obj.credit_score >= 600 and obj.marital_status!= 'Married'

# Create an instance of Client with income=75000, credit_score=720, marital_status='Divorced'
client = Client(75000, 720, 'Divorced')

# Call the is_suitable function on the client object
result = is_suitable(client)

# Print the result
print(result)  # Output: True
```

In this solution, we define a class `Client` with attributes `income`, `credit_score`, and `marital_status`. We then implement a method `is_suitable`