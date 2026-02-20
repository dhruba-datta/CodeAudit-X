# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj['income'] > 60000 and obj['credit_score'] >= 700

# Test the function with given data points
obj1 = {'income': 80000, 'credit_score': 730}
obj2 = {'income': 65000, 'credit_score': 710}

print(is_suitable(obj1))  # Expected output: True
print(is_suitable(obj2))  # Expected output: False
```
In this solution, the `is_suitable` function checks if a client's income exceeds $60,000 and their credit score is at least 700. The function returns `True`