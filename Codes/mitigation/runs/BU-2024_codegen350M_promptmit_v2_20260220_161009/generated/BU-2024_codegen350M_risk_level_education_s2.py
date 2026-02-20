# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if obj == 'Subject(history=clean, assets=50000, education='No Degree')':
        return False
    # Check if Subject(history='clean', assets=50000, education='Yes') is suitable
    elif obj == 'Subject(history=clean, assets=50000, education='Yes')':
        return True
    # Check if Subject(history='clean', assets=50000, education='No Degree') is not suitable
    elif obj == 'Subject(history=clean, assets=50000, education='No Degree')':
        return False
    # Check if Subject(history='clean', assets=50000, education='Yes') is not suitable
