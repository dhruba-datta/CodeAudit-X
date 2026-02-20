# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     return obj['income'] > 60000 and obj['credit_score'] > 710

# Test the function with a sample object
obj = {'income': 75000, 'credit_score': 720}
print(is_suitable(obj))  # Output should be True if the client is suitable, False otherwise
```

In this solution, the `is_suitable` function checks if an individual's income is greater than 60,000 and their credit score is greater than 710. This is a simple criterion that can be applied to any set of data points representing individuals' financial health and creditworthiness. The function returns `True` if the individual