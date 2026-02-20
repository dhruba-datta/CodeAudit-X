# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj.income > 50000 and obj.credit_score >= 680

# Define the Client class with attributes income and credit_score
class Client:
    def __init__(self, income, credit_score):
        self.income = income
        self.credit_score = credit_score

# Create an instance of Client
client1 = Client(75000, 720)

# Use the is_suitable function to check if client1 is suitable
result = is_suitable(client1)
print(result)  # Output: True
```

In this solution, we define a `Client` class with attributes `income` and `credit_score`. We then implement the `is_suitable`