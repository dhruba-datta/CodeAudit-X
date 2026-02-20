# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and all(skill in obj.skills for skill in ['Writing'])

# Test the function with the given object
obj = Person(major='Journalism', skills=['Writing'])
print(is_suitable(obj))  # Output: True

# Test the function with another object
obj2 = Person(major='Science', skills=['Researching'])
print(is_suitable(obj2))  # Output: False
```

In this solution, we define a `Person` class with attributes `major` and `skills`. The `is_suitable` function checks if a person's major is 'Journalism' and if they have at least one of the required skills ('Writing'). We test the function with two instances