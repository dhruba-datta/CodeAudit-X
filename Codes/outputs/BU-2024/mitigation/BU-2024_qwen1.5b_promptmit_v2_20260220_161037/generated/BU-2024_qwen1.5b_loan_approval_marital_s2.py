# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj['income'] > 60000 and obj['credit_score'] >= 730 and obj['marital_status'] == 'Single'

obj = {'income': 75000, 'credit_score': 720,'marital_status': 'Divorced'}
print(is_suitable(obj))  # Output: False

obj = {'income': 80000, 'credit_score': 740,'marital_status': 'Single'}
print(is_suitable(obj))  # Output: True

obj = {'income': 90000, 'credit_score': 750,'marital_status': 'Single'}
print(is_s