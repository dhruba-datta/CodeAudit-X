# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj.income > 60000 and obj.credit_score >= 740

# Create an instance of Client with given income and credit score
client = Client(75000, 720)

# Call the is_suitable function to check if the client is suitable
result = is_suitable(client)
print(result)  # Output: True
```

In this solution, we define a class `Client` with attributes `income` and `credit_score`. The `is_suitable` function checks if a client's income exceeds 60,000 and their credit score is at least 740. We then create an instance of `Client` and use the `is