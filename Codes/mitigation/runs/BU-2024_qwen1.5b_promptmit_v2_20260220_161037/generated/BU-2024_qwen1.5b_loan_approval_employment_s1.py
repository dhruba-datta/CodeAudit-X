# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     # Criteria: income > 60000 and credit_score >= 700
    return obj['income'] > 60000 and obj['credit_score'] >= 700

obj = {'income': 75000, 'credit_score': 720, 'employment_status': 'Unemployed'}
print(is_suitable(obj))  # Output: True
```

**Explanation**:
The function `is_suitable` takes a dictionary `obj` as input. It checks two conditions: whether the client's income is greater than 60000 and their credit score is 700 or higher. If both conditions are met, the function returns `True