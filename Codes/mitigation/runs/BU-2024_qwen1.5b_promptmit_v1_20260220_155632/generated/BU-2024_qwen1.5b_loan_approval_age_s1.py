# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.age >= 30 and obj.credit_score >= 700 and obj.income > 50000

# Create an instance of Client with the given attributes
client = Client(income=75000, credit_score=720, age=65)

# Call the is_suitable function with the client object as an argument
result = is_suitable(client)

# Print the result
print(result)
```

In this code snippet:
- The `is_suitable` function checks if a given `Client` object meets certain criteria: age must be at least 30, credit score must be at least 700, and income must be greater than 500