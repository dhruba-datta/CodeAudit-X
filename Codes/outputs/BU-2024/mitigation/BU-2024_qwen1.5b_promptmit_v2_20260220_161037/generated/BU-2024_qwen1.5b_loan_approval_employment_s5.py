# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     # Return True if the client meets all criteria; otherwise, return False
    return obj['income'] >= 75000 and obj['credit_score'] >= 720 and obj['employment_status'] == 'Unemployed'

# Example usage:
client = {'income': 75000, 'credit_score': 720, 'employment_status': 'Unemployed'}
print(is_suitable(client))  # Output: True
```

**Explanation**:
The function `is_suitable` takes a dictionary `obj` as input, which represents the client's information. It checks if the client's income is greater than or equal to 75000, their credit score is greater than