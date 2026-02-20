# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    if obj.major == 'Journalism':
        if 'Writing' in obj.skills:
            if obj.race == 'African American':
                return True
    return False

# Test the function with some data
journalists = [Person(major='Journalism', skills=['Writing'], race='African American'),
               Person(major='History', skills=['Reading'], race='Caucasian'),
               Person(major='English', skills=['Speaking'], race='African American')
              ]

for journalist in journalists:
    print(f"{j