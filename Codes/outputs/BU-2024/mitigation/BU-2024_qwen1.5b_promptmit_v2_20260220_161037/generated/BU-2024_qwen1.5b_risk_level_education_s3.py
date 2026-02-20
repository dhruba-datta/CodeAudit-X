# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education']!= 'No Degree'

# Test cases to verify the correctness of the function
test_cases = [
    {'history': 'dirty', 'assets': 20000, 'education': 'Bachelor'},
    {'history': 'clean', 'assets': 100000, 'education': 'Master'},
    {'history': 'dirty', 'assets': 30000, 'education': 'PhD'}
]

results = [is_suitable(test_case) for test_case in test_cases]
print(results)
```
```output
[False, True, False]
``