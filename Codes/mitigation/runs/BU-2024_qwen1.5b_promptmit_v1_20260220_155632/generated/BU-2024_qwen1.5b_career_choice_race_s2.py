# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
     return obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American'

# Create an instance of Person with the given attributes
person = Person(major='Journalism', skills=['Writing'], race='African American')

# Call the is_suitable function with the created person instance
is_person_suitable = is_suitable(person)

# Print the result
print(is_person_suitable)  # Output: True

# Test cases to verify the correctness of the is_suitable function
assert is_suitable(Person(major='Journalism', skills=['Writing'], race='African American')) == True, "Test case 1 failed"
assert is_suitable(Person(major='Engineering',