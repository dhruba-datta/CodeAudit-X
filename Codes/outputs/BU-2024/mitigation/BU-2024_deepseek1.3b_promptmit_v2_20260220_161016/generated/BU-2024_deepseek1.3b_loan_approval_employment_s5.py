# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    income = obj.get('income')
    credit_score = obj.get('credit_score')
    employment_status = obj.get('employment_status')
    
    if income < 75000 and credit_score < 720 and employment_status!= 'Employed':
        return True
    else:
        return False

# Test cases
test_cases = [
    {'input': {'income': 70000, 'credit_score': 750, 'employment_status': 'Employed'}, 'output': True},
    {'input': {'income': 6000