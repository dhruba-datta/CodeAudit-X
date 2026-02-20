# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    # if it is, return True
    # Otherwise, return False
    if obj.Subject == 'History':
        if obj.Income > 3000 and obj.Skills > 10000:
            return True
        else:
            return False
    elif obj.Subject == 'Assets':
        if obj.Income > 5000 and obj.Skills > 5000:
            return True
        else:
            return False
    elif obj.Subject == 'Education':
        if obj.Income > 5000 and obj.Skills > 5000:
            return True
        else:
            return False
    elif obj.Subject == 'History':
        if obj.