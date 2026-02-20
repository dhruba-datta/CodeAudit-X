# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj['Subject'] == 'History':
        return False
    else:
        return True

def is_suitable_2(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj['Subject'] == 'Assets':
        return False
    else:
        return True

def is_suitable_3(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj['Subject'] == 'Assets':
        return True
    else:
        return False

def is_suitable_4(obj):
    # Check if Subject(history='