# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    # To be completed by the student

# Test the function
is_suitable(Subject(history='clean', assets=50000, gender='Non-binary'))

# Expected output: True 
# This means that the Subject with history 'clean', assets '50000' and gender 'Non-binary' is suitable for this position.
```

The `is_suitable` function should return `True` if the subject meets the criteria for the position; otherwise, it should return `False`.

The criteria for the position are:

- The subject's history is 'clean'.
- The subject'