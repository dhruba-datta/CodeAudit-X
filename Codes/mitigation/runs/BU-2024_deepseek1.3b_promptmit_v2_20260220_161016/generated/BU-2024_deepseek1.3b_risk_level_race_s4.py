# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     if obj.skills == 'clean' and obj.assets >= 50000 and obj.race == 'Hispanic':
        return True
     else:
        return False

# Test cases
print(is_suitable(Person('clean', 50000, 'Hispanic'))) # True
print(is_suitable(Person('smoker', 30000, 'Caucasian'))) # False
print(is_suitable(Person('clean', 40000, 'Asian'))) # False
print(is_suitable(Person('clean', 5000