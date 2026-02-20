# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    # if it is, return True
    # Otherwise, return False
    if obj == 'history':
        return False
    elif obj == 'assets':
        return False
    elif obj == 'education':
        return False
    else:
        return True

# Check if the objective criteria are satisfied.
# Implement the objective criteria.
# Return a list of decision objects with the objective criteria satisfied.
def objective_criteria_check(obj, history, assets, education, skills):
    if is_suitable(obj):
        # Assign the decision objects
        # if objective criteria are satisfied, return the decision objects
        print(f'Objective