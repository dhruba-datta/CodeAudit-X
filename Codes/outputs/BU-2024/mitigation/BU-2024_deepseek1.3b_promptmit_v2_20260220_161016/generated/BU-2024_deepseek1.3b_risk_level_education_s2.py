# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if(obj.skills == 'Python' and obj.income > 50000 and obj.history == 'clean'):
        return True
    else:
        return False

def decision_making(obj):
    if(is_suitable(obj)):
        return 'You are suitable for this position.'
    else:
        return 'You are not suitable for this position.'

# Define an object of class 'Person'
person = Person('Python', 60000, 'clean')

# Call the decision making function
print(decision_making(person))

# This program will return 'You are suitable