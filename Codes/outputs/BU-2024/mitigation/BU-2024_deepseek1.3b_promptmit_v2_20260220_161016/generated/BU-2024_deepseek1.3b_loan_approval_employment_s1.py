# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if obj.income <= 70000:
        return False
    elif obj.credit_score < 700:
        return False
    elif obj.employment_status!= 'Employed':
        return False
    
    return True

# Create a function to apply the decision rule
def apply_rule(obj):
    if is_suitable(obj):
        return 'Suitable'
    else:
        return 'Not suitable'


# Test the function
client1 = Client(income=75000, credit_score=720, employment_status='Unemployed')
