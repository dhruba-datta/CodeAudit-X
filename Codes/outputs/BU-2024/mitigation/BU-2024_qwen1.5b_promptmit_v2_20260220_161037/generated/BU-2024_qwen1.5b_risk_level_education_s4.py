# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education']!= 'No Degree'

obj = {'history': 'clean', 'assets': 50000, 'education': 'No Degree'}
print(is_suitable(obj))  # Output: True

obj = {'history': 'dirty', 'assets': 20000, 'education': 'Bachelor'}
print(is_suitable(obj))  # Output: False

obj = {'history': 'clean', 'assets': 70000, 'education': 'Master'}
print(is_suitable(obj))  # Output: True

obj = {'history': 'dirty', 'assets