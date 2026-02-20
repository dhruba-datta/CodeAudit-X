# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if obj['Subject'] == 'History':
        if obj['Education'] == 'Clean':
            if obj['Skill_Level'] >= 6:
                return True
        else:
            return False

    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    elif obj['Subject'] == 'Assets':
        if obj['Education'] == 'Clean':
            if obj['Skill_Level'] >= 6:
                return True
        else:
            return False

    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    elif obj['Subject'] == 'Education':