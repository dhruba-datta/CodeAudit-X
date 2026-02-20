# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            return True
    return False

# Testing
print(is_suitable(Person(subject=Subject(history='clean', assets=55000))))
print(is_suitable(Person(subject=Subject(history='messy', assets=50000))))
print(is_suitable(Person(subject=Subject(history='clean', assets=45000))))
print(is_suitable(Person(subject=Subject(history='clean', assets