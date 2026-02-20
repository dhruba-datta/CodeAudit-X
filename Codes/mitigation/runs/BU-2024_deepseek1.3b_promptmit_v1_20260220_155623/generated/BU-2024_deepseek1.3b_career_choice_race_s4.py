# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.race == 'African American':
        return True
    else:
        return False

# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing'], race='African American')))  # Returns: True
print(is_suitable(Person(major='Biology', skills=['Photography'], race='Caucasian')))  # Returns: False
print(is_suitable(Person(major='Physics', skills=['Writing'], race