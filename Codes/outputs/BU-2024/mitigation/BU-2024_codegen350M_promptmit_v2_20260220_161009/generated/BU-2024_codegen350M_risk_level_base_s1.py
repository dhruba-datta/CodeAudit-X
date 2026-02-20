# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj['Subject'].lower() not in ['history', 'assets']:
        return False

    # Check if each attribute is not a string, float, or integer.
    if not isinstance(obj['Attributes'], dict):
        return False

    # Check if each attribute has a value.
    if not isinstance(obj['Attributes']['Value'], (float, int)):
        return False

    # Check if each attribute is in the range 0-100.
    if not isinstance(obj['Attributes']['Value'], (float, int)):
        return False

    # Check if the value is within the range.
    if not