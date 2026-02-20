# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj['income'] > 60000 and obj['credit_score'] >= 710 and obj['employment_status']!= 'Employed'

obj = {'income': 75000, 'credit_score': 720, 'employment_status': 'Unemployed'}
print(is_suitable(obj))  # Output: True

obj = {'income': 40000, 'credit_score': 680, 'employment_status': 'Employed'}
print(is_suitable(obj))  # Output: False

obj = {'income': 90000, 'credit_score': 730, 'employment_status': 'Employed'}
print(is_suitable(obj