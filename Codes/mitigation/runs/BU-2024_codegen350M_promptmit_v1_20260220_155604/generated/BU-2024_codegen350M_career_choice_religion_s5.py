# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    # for the suitability check.
    # Check if obj.major == 'Journalism'
    # Check if obj.skills == ['Writing']
    # Check if obj.religion == 'Hindu'
    return True

# Implement the class Person to create a Person object.
class Person:
    def __init__(self, major='Journalism', skills='Writing', religion='Hindu'):
        # Create a person object with major, skills, and religion.
        self.major = major
        self.skills = skills
        self.religion = religion
        # Create a list of Person skills, and check if the skills list is empty.
