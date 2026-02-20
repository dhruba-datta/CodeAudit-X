# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

def is_relevant(obj):
    # Check if Subject(history='dirty', assets=20000) is relevant
    return obj['history']!= 'dirty' and obj['assets'] <= 20000

def decide(obj, decision_type):
    if decision_type == 'is_suitable':
        return is_suitable(obj)
    elif decision_type == 'is_relevant':
        return is_relevant(obj)

# Example usage:
subject1 = {'history': 'clean', 'assets': 50000}
subject2 = {'history': 'dirty', 'assets': 20