# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj.income > 50000 and obj.credit_score >= 680

# Create an instance of Client class with given income and credit score
client = Client(75000, 720)

# Call the is_suitable function to check the suitability of the client
result = is_suitable(client)

# Print the result
print(result)  # Output: True
```

In this solution, we define a `Client` class with attributes `income` and `credit_score`. The `is_suitable` function checks if the client's income is greater than 50,000 and their credit score is at least 680. We then create an instance of