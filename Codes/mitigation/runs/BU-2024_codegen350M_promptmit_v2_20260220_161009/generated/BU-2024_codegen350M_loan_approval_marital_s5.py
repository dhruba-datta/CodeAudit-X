# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    # for the objective function.
    if obj['income'] < 75000 and obj['credit_score'] < 720 and obj['marital_status'] == 'Divorced':
        return True
    return False

# The objective function for the Decision Logic.
# The objective is to determine whether the employee has to take a loan to the company.
# In this case, the objective is to determine whether the employee has to take a loan to the company.
# If the employee is not eligible to take a loan, then the objective is to determine whether the employee has to take a loan to the company.
# In this case, the objective is to determine whether the employee has to take a loan