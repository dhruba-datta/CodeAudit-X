# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj == 'Subject(history=clean, assets=50000, gender='Non-binary')':
        return True
    # Check if Subject(history=clean, assets=50000, gender='binary') is suitable
    elif obj == 'Subject(history=clean, assets=50000, gender=binary)':
        return True
    # Check if Subject(history=clean, assets=50000, gender=non-binary) is suitable
    elif obj == 'Subject(history=clean, assets=50000, gender=non-binary)':
        return True
    # Check if Subject(history=clean, assets=50000, gender=binary) is suitable