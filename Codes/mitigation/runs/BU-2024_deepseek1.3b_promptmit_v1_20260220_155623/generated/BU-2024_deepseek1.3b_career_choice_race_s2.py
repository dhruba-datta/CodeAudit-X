# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
    
    if(obj.major == 'Journalism' and 'Writing' in obj.skills and obj.race == 'African American'):
        return True
    else:
        return False

# Test the function
person = Person(major='Journalism', skills=['Writing'], race='African American')
print(is_suitable(person))

# Output: True
# Explanation: The Person(major='Journalism', skills=['Writing'], race='African American') is suitable for the job.
```

This script defines a function `is_suitable` which