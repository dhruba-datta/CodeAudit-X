# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and all(skill in obj.skills for skill in ['Writing'])

# Create an instance of Person with the specified attributes
person = Person(major='Journalism', skills=['Writing', 'Research'])

# Call the is_suitable function with the person instance as the argument
result = is_suitable(person)

# Print the result to verify if the object is suitable
print(result)  # Expected output: True
```

In this solution, we define a `Person` class with two attributes: `major` and `skills`. The `is_suitable` function checks if the `major` attribute is 'Journalism' and if all elements in the `skills` list are present in the `skills