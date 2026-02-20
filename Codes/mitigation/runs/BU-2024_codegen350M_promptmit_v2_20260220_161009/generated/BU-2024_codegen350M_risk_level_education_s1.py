# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    if obj['Subject'].lower() not in ['history', 'assets', 'education', 'education-no-degree']:
        return False

    # Check if skill(s) are eligible
    # Skip any non-skill skills
    if obj['skills'] == 'None':
        return False

    # Check if skill level is either 'None' or '1'
    # Skip any skill level > 3
    if obj['skills'].find('None') > -1:
        return False

    # Check if skill level is either '2' or '3'
    # Skip any skill level > 3
    if obj['skills'].find('2