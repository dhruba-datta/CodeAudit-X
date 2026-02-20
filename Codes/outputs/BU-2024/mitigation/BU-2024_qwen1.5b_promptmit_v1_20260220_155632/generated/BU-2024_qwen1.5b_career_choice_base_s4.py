# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and len(obj.skills) >= 2

# Test the function with a Person object
person = Person(major='Journalism', skills=['Writing'])
print(is_suitable(person))  # Output: True

# Create another Person object
another_person = Person(major='Science', skills=['Reading'])
print(is_suitable(another_person))  # Output: False

# Create yet another Person object
yet_another_person = Person(major='Engineering', skills=['Programming'])
print(is_suitable(yet_another_person))  # Output: False
```

In this solution, we define a `Person` class with attributes `major` and `skills`. The `is_suitable`