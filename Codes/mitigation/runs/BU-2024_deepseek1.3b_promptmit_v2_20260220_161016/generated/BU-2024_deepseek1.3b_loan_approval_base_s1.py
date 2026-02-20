# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if obj.income <= 70000:
        return False
    elif obj.credit_score < 700:
        return False
    elif obj.skills.split(',') not in ['Python', 'Java', 'C++']:
        return False
    else:
        return True

# Test data
clients = [
    Client(income=60000, credit_score=800, skills='Python'),
    Client(income=75000, credit_score=720, skills='Java'),
    Client(income=55000, credit_