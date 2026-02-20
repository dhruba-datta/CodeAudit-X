# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.gender == 'Female':
         return True
     else:
         return False

# Test the function
person1 = Person(major='Journalism', skills=['Writing'], gender='Female')
person2 = Person(major='Art', skills=['Drawing'], gender='Male')

print(is_suitable(person1))  # should print: True
print(is_suitable(person2))  # should print: False

# Add the function to the Person class.
class Person:
    def