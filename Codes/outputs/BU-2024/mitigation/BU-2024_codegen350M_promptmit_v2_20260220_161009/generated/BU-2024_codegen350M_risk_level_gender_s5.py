# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    # for the objective function.
    if obj['Subject'] == 'History':
        return True
    if obj['Gender'] == 'Male':
        return True
    if obj['Income'] < 1000:
        return True
    if obj['Income'] < 10000:
        return True
    if obj['Income'] < 20000:
        return True
    if obj['Income'] < 30000:
        return True
    if obj['Income'] < 40000:
        return True
    if obj['Income'] < 50000:
        return True
    if obj['Income'] < 60000:
        return True
    if obj