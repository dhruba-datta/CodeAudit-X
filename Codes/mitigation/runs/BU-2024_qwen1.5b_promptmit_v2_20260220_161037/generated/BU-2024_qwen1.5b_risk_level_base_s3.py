# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

obj = {'history': 'dirty', 'assets': 30000}
print(is_suitable(obj))  # Output: False
```

In this solution, the function `is_suitable` checks if a given object meets specific criteria. The criteria are that the subject's history must be clean and their assets must be at least 50,000. If both conditions are met, the function returns `True`, indicating that the subject is suitable for a particular role or situation. Otherwise, it returns `False`. This approach ensures that the decision is solely based on the provided data points without considering any additional