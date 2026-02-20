# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['education'] == 'No Degree'
     
obj = {'history': 'dirty', 'assets': 40000, 'education': 'Bachelor'}
print(is_suitable(obj))  # Output: False

obj = {'history': 'clean', 'assets': 60000, 'education': 'Master'}
print(is_suitable(obj))  # Output: True

obj = {'history': 'dirty', 'assets': 30000, 'education': 'Bachelor'}
print(is_suitable(obj))  # Output: False

obj = {'history': 'clean', 'assets