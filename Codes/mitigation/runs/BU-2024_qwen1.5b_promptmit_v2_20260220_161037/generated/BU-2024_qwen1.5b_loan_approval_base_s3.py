# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj['income'] >= 75000 and obj['credit_score'] >= 720

# Test the function with sample data
sample_data = {'income': 75000, 'credit_score': 720}
print(is_suitable(sample_data))  # Output should be True
```

**Explanation**:
The `is_suitable` function takes a dictionary `obj` as input, which represents an individual's profile. It checks two conditions:
1. The individual's income must be greater than or equal to 75,000.
2. The individual's credit score must be greater than or equal to 720.

If both conditions are met, the function