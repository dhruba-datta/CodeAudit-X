# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    if obj.income <= 60000 or obj.credit_score <= 650:
        return False # The client is not suitable
    elif obj.skills.count('Python') < 1 or obj.skills.count('C++') < 1:
        return False # The client is not suitable
    elif obj.skills.count('Java') < 1:
        return False # The client is not suitable
    else:
        return True # The client is suitable

# Test the function
print(is_suitable(Client(income=75000, credit_score=720, age=65,