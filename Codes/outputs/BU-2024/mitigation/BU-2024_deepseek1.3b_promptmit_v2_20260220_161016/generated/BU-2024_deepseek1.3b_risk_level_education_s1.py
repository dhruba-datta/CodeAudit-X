# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if obj.skills == 'Python' and obj.income <= 50000 and obj.education == 'Diploma':
        return True
    else:
        return False

# Demo usage
person1 = Person(skills='Python', income=60000, education='Diploma', history='clean')
person2 = Person(skills='Java', income=40000, education='No Degree', history='old')

print(is_suitable(person1))  # Should print True
print(is_suitable(person2))  # Should print False