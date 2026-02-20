# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    if (obj['income'] < 5000 and obj['credit_score'] >= 720) or (obj['credit_score'] < 720 and obj['income'] < 5000):
        return True
    else:
        return False

def is_suitable_skills(obj):
    # Check if the client has skills for at least 1 and at most 4
    if obj['skills'] >= 4 and obj['skills'] <= 5:
        return True
    else:
        return False

def is_suitable_skills_and_income(obj):
    # Check if the client has skills for at least 1 and at most 4
    if obj['skills