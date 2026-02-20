# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     return obj.age > 60 and obj.credit_score >= 730

# Create an instance of Client
client = Client(income=75000, credit_score=720, age=65)

# Call the is_suitable function with the client object as an argument
result = is_suitable(client)
print(result)  # Output: False
```

In this solution, we define a `Client` class to represent individuals with attributes such as income, credit score, and age. The `is_suitable` function checks if a client meets certain criteria (age greater than 60 and credit score greater than or equal to 730). We create an instance of `Client` and