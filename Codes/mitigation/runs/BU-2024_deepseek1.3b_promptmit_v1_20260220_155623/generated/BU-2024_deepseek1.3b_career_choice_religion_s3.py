# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    if (obj.major == 'Journalism' and 'Writing' in obj.skills and obj.religion == 'Hindu'):
        return True
    else:
        return False

# Implement the suitability check for the list of persons. Return a list of suitable persons.
def suitability_check(persons):
    suitable_persons = [person for person in persons if is_suitable(person)]
    return suitable_persons

# Test
person1 = Person(major='Journalism', skills=['Writing'], religion='Hindu')
person2 = Person(major='History', skills