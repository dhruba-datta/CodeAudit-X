# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

# Test the function with a sample object
obj = {'history': 'clean', 'assets': 50000, 'income': 60000}
print(is_suitable(obj))  # Output should be True if the subject meets the criteria
```

In this solution, the `is_suitable` function checks if the given object's history is 'clean' and its assets are greater than or equal to 50,000. The test case demonstrates how the function can be used to determine if a subject is suitable for a particular role based on their financial and professional background. This approach