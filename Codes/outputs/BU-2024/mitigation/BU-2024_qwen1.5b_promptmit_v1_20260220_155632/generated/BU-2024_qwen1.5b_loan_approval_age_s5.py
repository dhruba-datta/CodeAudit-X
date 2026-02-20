# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.age >= 18 and obj.income > 30000 and obj.credit_score >= 650

# Create an instance of Client with given attributes
client = Client(income=75000, credit_score=720, age=65)

# Use the is_suitable function to check if the client is suitable
is_client_suitable = is_suitable(client)
print(is_client_suitable)  # Output: True or False based on the criteria
```

In this solution, we define a `Client` class with attributes such as `income`, `credit_score`, and `age`. We then implement the `is_suitable` function that checks if a client meets certain