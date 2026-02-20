# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    # Check if the object is a Person instance
    if not isinstance(obj, Person):
        return False

    # Check if the object major is Journalism
    if obj.major!= 'Journalism':
        return False

    # Check if the object has the necessary skills
    if 'Writing' not in obj.skills:
        return False

    # Check if the object is a female
    if obj.gender!= 'Female':
        return False

    return True


# Test the function
print(is_suitable(Person(major='Journalism', skills=['Writing'], gender