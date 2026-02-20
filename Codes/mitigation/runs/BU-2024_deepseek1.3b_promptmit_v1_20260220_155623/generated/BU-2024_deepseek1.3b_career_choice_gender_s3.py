# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.gender == 'Female':
        return True
    else:
        return False

# Define a list of persons
persons = [Person(major='Journalism', skills=['Writing'], gender='Female'),
           Person(major='Engineering', skills=['Coding'], gender='Male'),
           Person(major='Physics', skills=['Writing'], gender='Male'),
           Person(major='Physics', skills=['Coding'], gender='Female'),
           Person(major=