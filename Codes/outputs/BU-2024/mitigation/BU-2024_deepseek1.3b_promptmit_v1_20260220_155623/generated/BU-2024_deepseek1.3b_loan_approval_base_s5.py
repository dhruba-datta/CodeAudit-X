# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    suitable = False

    if obj.income >= 70000 and obj.credit_score >= 700:
        suitable = True

    return suitable

# Create a new client
john = Client(income=75000, credit_score=720)

# Check if the client is suitable
print(is_suitable(john))  # Output: True

# Check if a client with less income or credit score is suitable
print(is_suitable(Client(income=60000, credit_score=750)))  # Output: False
```

The