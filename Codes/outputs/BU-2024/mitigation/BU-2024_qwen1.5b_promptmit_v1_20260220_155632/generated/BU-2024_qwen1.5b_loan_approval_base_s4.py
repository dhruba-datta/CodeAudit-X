# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj.income >= 75000 and obj.credit_score >= 720

# Create an instance of Client with income=74999 and credit_score=719
client = Client(74999, 719)

# Call the is_suitable function to check if the client is suitable
result = is_suitable(client)
print(result)  # Output: False
```

In this solution, we define a `Client` class with attributes `income` and `credit_score`. The `is_suitable` function checks if the client's income is greater than or equal to 75000 and their credit score is greater than or equal to 72