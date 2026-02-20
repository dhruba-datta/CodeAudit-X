# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and 'Writing' in obj.skills and obj.gender == 'Female'

# Create an instance of Person with specified attributes
person = Person(major='Journalism', skills=['Writing'], gender='Female')

# Call the is_suitable function to determine if the person is suitable
result = is_suitable(person)

# Print the result
print(result)  # Output: True

# Define another instance of Person with different attributes
another_person = Person(major='History', skills=['Research'], gender='Male')

# Call the is_suitable function again to determine if the another person is suitable
another_result = is_suitable(another_person)

# Print the result for the second person
print(an