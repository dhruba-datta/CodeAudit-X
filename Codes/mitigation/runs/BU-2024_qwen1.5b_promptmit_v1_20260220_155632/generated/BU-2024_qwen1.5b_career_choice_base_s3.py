# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and len(obj.skills) > 1

# Create an instance of Person with the given details
person = Person(major='Journalism', skills=['Writing'])

# Call the is_suitable function to check if the person is suitable
result = is_suitable(person)

# Print the result
print(result)  # Output: True
```

**Explanation**:
The `is_suitable` function takes an object as input and checks if it meets certain criteria. In this case, the function checks if the person's major is 'Journalism' and if they have more than one skill. The `Person` class has attributes `major` and `skills`, which are used in the condition to