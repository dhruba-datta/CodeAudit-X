# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills:
        return True
    else:
        return False

# Implement the filter function.
def filter_people(people):
    # Filter people by their suitability
    suitable_people = []
    for person in people:
        if is_suitable(person):
            suitable_people.append(person)
    return suitable_people

# Test the function
journalism_people = [Person(major='Journalism', skills=['Writing']),
                     Person(major='Science', skills=['Writing', 'Reading