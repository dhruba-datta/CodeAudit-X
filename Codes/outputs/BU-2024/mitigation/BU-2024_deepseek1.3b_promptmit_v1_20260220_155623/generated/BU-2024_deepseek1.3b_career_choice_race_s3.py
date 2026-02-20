# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.race == 'African American':
        return True
    else:
        return False

# Create a list of people
people = [
    Person(major='Journalism', skills=['Writing'], race='African American'),
    Person(major='Biology', skills=['Photography'], race='Asian'),
    Person(major='Art', skills=['Drawing'], race='Caucasian'),
]

# Use the is_suitable function to filter out the suitable people
suit