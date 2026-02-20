# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if (obj['income'] < 5000 and obj['credit_score'] >= 80) or (obj['credit_score'] < 80 and obj['marital_status'] == 'Married-couple'):
        return True
    else:
        return False

# Check if the objective function is the same as the objective function for the given decision variable
def is_same_objective(obj1, obj2):
    # obj1 and obj2 are dictionaries
    # Check the objective function
    if obj1['income'] < 5000 and obj1['credit_score'] >= 80 and obj1['marital_status'] == 'Married-couple':
        return