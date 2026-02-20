# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and len(obj.skills) > 0 and obj.gender == 'Female'

# Create an instance of Person
person = Person(major='Journalism', skills=['Writing'], gender='Female')

# Call the is_suitable function with the person object as an argument
result = is_suitable(person)

# Print the result
print(result)
```

**Explanation**:
The `is_suitable` function takes an object as input and checks if it meets certain criteria. In this case, the function checks if the person's major is 'Journalism', they have at least one skill, and their gender is 'Female'. If all these conditions are met, the function returns `True`, indicating that the