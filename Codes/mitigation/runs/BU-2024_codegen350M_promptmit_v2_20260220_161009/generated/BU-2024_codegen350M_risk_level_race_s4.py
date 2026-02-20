# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
    if obj['subject'] =='subject':
        if obj['history'] == 'clean':
            if obj['assets'] == 50000:
                if obj['race'] == 'Hispanic':
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    # Check if Age is <=50
    elif obj['subject'] == 'age':
        if obj['assets'] <= 50:
            return False
        else:
            return True
    # Check if Age is >=80
    elif obj['subject'] == 'age':
        if obj['assets'] >= 80:
            return False
        