# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and obj.gender == 'Female' and 'Writing' in obj.skills

# Create an instance of Person with specified attributes
person = Person(major='Journalism', skills=['Writing'], gender='Female')

# Call the is_suitable function to check if the person is suitable
is_person_suitable = is_suitable(person)

# Print the result
print(is_person_suitable)  # Output: True or False based on the criteria
```

In this solution, we define a `Person` class with attributes such as `major`, `skills`, and `gender`. The `is_suitable` function checks if a given `Person` object meets specific criteria: major should be 'Journalism