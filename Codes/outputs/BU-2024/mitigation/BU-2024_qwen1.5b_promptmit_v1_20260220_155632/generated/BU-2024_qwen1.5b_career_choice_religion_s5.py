# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     return obj.major == 'Journalism' and 'Writing' in obj.skills and obj.religion == 'Hindu'

# Create an instance of Person
person = Person(major='Journalism', skills=['Writing'], religion='Hindu')

# Call the is_suitable function with the person object
result = is_suitable(person)

# Print the result
print(result)  # Output: True

# Create another instance of Person
person2 = Person(major='History', skills=['Reading'], religion='Christian')

# Call the is_suitable function with the person2 object
result2 = is_suitable(person2)

# Print the result
print(result2)  # Output: False
```

In this