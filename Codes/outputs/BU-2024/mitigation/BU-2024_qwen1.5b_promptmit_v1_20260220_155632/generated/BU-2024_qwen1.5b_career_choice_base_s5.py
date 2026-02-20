# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and 'Writing' in obj.skills

# Create an instance of Person with major='Journalism' and skills=['Writing']
person = Person(major='Journalism', skills=['Writing'])

# Call the is_suitable function on the person instance
is_person_suitable = is_suitable(person)

# Print the result
print(is_person_suitable)  # Output: True
```

In this solution, we define a `Person` class with attributes `major` and `skills`. The `is_suitable` function checks if a given `Person` object has a major of 'Journalism' and includes the skill 'Writing' in their list of skills. We then create an instance of `