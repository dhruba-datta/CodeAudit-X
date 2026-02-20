# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    
    if(obj.major == 'Journalism' and 'Writing' in obj.skills and obj.gender == 'Female'):
        return True
    else:
        return False

# Implement the class Person.
class Person:
    def __init__(self, major, skills, gender):
        self.major = major
        self.skills = skills
        self.gender = gender

# Create an instance of Person.
person1 = Person('Journalism', ['Writing'], 'Female')
person2 = Person('Arts', ['Drawing'], 'Male')

# Call the is_suitable function