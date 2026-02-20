# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     # Check if Subject(history='dirty', assets=20000, education='Bachelor's') is suitable
    # Return True if subject is suitable, False otherwise

    if obj['history'] == 'clean' and obj['assets'] > 30000 and obj['education'] == 'No Degree':
        return True
    elif obj['history'] == 'dirty' and obj['assets'] < 10000 and obj['education'] == 'Bachelor's':
        return True
    else:
        return False

obj = {'history': 'dirty', 'assets': 15000, 'education': 'Bachelor's'}
print(is_suitable(obj))  # Output should