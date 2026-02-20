# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            if obj.religion == 'Hindu':
                return True
    return False


# Test the function with some data
journalist = Person(major='Journalism', skills=['Writing'], religion='Hindu')
print(is_suitable(journalist))  # Should print True

student = Person(major='Physics', skills=['Reading'], religion='Buddhist')
print(is_suitable(student))  # Should print False

citizen = Person(