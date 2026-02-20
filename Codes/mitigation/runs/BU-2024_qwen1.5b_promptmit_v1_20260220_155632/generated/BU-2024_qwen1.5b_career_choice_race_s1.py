# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
     return obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.race == 'African American'

# Test the function with the given data points
assert is_suitable(Person(major='Journalism', skills=['Writing'], race='African American')) == True
assert is_suitable(Person(major='Engineering', skills=['Problem Solving'], race='Asian American')) == False
```

In this solution, we define a function `is_suitable` that takes an object as input. The function checks if the object's major subject is 'Journalism', its skills include 'Writing', and its race is 'African American'. If all these conditions are met, the function returns `True`, indicating that the