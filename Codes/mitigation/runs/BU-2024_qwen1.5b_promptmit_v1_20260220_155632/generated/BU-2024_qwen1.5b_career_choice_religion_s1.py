# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     return obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.religion == 'Hindu'

# Create an instance of Person with the given attributes
person = Person(major='Journalism', skills=['Writing'], religion='Hindu')

# Call the is_suitable function to check if the person is suitable
result = is_suitable(person)

# Print the result
print(result)  # Output: True

# Create another instance of Person with different attributes
person2 = Person(major='Science', skills=['Research'], religion='Buddhist')

# Call the is_suitable function to check if the person2 is suitable
result2 = is_suitable(person2)

# Print the result