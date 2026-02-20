# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.income >= 75000 and obj.credit_score >= 720 and obj.age <= 65

# Create an instance of Client with income=75000, credit_score=720, age=65
client = Client(75000, 720, 65)

# Call the is_suitable function to check if the client is suitable
is_client_suitable = is_suitable(client)
print(is_client_suitable)  # Output: True or False depending on the criteria
```

**Explanation**:
In this solution, we define a `Client` class with attributes for income, credit score, and age. The `is_suitable