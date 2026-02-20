# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    # if it meets the objective criteria
    # return True
    if obj[0] == "Client" and obj[1] == "income" and obj[2] == "credit_score" and obj[3] == "income":
        return True
    return False

# Check if Client(income=75000, credit_score=720) is suitable
def is_suitable_with_inc_credit(obj):
    if obj[0] == "Client" and obj[1] == "income" and obj[2] == "credit_score" and obj[3] == "inc_credit":
        return True
    return False

# Check if