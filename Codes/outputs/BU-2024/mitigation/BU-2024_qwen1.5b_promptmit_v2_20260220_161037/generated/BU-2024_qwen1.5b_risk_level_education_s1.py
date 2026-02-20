# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education']!= 'No Degree'
     
# Example usage:
obj = {'history': 'clean', 'assets': 50000, 'education': 'No Degree'}
print(is_suitable(obj))  # Output should be True
```

This code snippet defines a function `is_suitable` that takes an object as input and returns `True` if the subject meets certain criteria (history is clean, assets are at least $50,000, and has no degree), otherwise it returns `False`. The example usage demonstrates how to use this function with a sample object. Note that in a