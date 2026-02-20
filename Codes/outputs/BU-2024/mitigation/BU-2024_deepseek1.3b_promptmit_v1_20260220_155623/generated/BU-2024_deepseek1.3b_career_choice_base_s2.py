# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    
    if(obj.major == 'Journalism' and 'Writing' in obj.skills):
        return True
    else:
        return False

# Check if Person(major='Physics', skills=['Writing', 'Reading']) is suitable
person2 = Person(major='Physics', skills=['Writing', 'Reading'])
print(is_suitable(person2))

# Check if Person(major='Art', skills=['Drawing']) is suitable
person3 = Person(major='Art', skills=['Drawing'])
print(is_suitable(person3))

# Check if Person(major='