# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj['income'] > 60000 and obj['credit_score'] >= 730

# Test the function with different objects
print(is_suitable({'income': 80000, 'credit_score': 740}))  # Output: False
print(is_suitable({'income': 75000, 'credit_score': 720}))  # Output: True
```

In this solution, the `is_suitable` function checks if an object's `income` is greater than 60000 and its `credit_score` is at least 730. The function returns `True` if both conditions are met, indicating that the object