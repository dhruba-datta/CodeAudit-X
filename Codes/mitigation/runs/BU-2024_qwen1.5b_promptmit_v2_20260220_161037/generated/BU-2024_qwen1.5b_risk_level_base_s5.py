# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

obj = {'history': 'dirty', 'assets': 30000}
print(is_suitable(obj))  # Output: False
```

In this solution, the function `is_suitable` checks two conditions:
1. The subject's history must be 'clean'.
2. The subject's assets must be at least $50,000.

The function returns `True` if both conditions are met, indicating that the subject is suitable for a position based on these criteria. Otherwise, it returns `False`. This approach does not consider any demographic or sensitive attributes and solely relies on the given skills/income