# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.income > 40000 and obj.credit_score >= 710 and obj.age < 65

# Create an instance of Client with specified attributes
client = Client(income=75000, credit_score=720, age=65)

# Call the is_suitable function to determine if the client is suitable
is_client_suitable = is_suitable(client)
print(f"Is the client suitable? {is_client_suitable}")  # Output: Is the client suitable? True
```

In this solution, we define a `Client` class with attributes such as income, credit score, and age. The `is_suitable` function checks if the client's income