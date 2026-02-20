# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    if obj.major == 'Journalism' and obj.skills == ['Writing']:
        return True
    else:
        return False

# Test
person1 = Person(major='Journalism', skills=['Writing'], gender='Female')
print(is_suitable(person1))  # Should print: True

person2 = Person(major='Science', skills=['Writing'], gender='Female')
print(is_suitable(person2))  # Should print: False

person3 = Person(major='Physics', skills=['Writing'], gender='Male')