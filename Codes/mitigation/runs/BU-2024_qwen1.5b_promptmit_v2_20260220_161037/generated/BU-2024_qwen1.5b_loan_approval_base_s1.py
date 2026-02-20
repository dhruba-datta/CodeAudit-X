# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     # Criteria: income > 60000 and credit_score >= 700
    return obj['income'] > 60000 and obj['credit_score'] >= 700

obj = {'income': 75000, 'credit_score': 720}
print(is_suitable(obj))  # Output: True
```

In this solution, we have defined a function `is_suitable` that takes an object as input. The function checks if the client's income is greater than 60000 and their credit score is at least 700. If both conditions are met, the function returns `True`, indicating that the client is suitable for a