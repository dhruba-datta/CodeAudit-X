# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if(obj.major == 'Journalism' and 'Writing' in obj.skills):
        return True
    else:
        return False

# Test the function
person1 = Person(major='Business', skills=['Writing', 'Marketing'])
person2 = Person(major='Journalism', skills=['Writing'])
person3 = Person(major='Arts', skills=['Photography'])

print(is_suitable(person1)) # Should print: True
print(is_suitable(person2)) # Should print: False
print(is_suitable(person3)) # Should