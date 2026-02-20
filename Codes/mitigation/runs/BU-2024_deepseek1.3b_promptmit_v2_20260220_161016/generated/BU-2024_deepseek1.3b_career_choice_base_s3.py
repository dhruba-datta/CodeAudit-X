# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills:
        return True
    else:
        return False

# Test
person1 = Person(major='Journalism', skills=['Writing', 'Reading'])
print(is_suitable(person1)) # Should return True

person2 = Person(major='Science', skills=['Writing', 'Photography'])
print(is_suitable(person2)) # Should return False

person3 = Person(major='Journalism', skills=['Writing'])
print(is_suitable(person3)) #