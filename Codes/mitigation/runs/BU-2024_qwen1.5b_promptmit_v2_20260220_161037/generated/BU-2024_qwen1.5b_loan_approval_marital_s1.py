# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     # Criteria: income > 60000 and credit_score >= 700
    return obj['income'] > 60000 and obj['credit_score'] >= 700

obj = {'income': 75000, 'credit_score': 720,'marital_status': 'Divorced'}
print(is_suitable(obj))  # Output: True
```

In this solution, the function `is_suitable` checks if a given client's income and credit score meet specific criteria to determine if they are suitable for a particular service. The criteria used in this example are that the client's income must be greater than 60,000 and their