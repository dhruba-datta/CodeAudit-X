# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     # Check if Client(income=60000, credit_score=680) is suitable
    # Return True if Client is suitable, False otherwise

    # Solution:
    if obj['income'] >= 75000 and obj['credit_score'] >= 720:
        return True
    else:
        return False

# Test cases to verify the correctness of the function
print(is_suitable({'income': 75000, 'credit_score': 720}))  # Expected output: True
print(is_suitable({'income': 60000, 'credit_score': 680}))  # Expected output: False
```

**Explanation