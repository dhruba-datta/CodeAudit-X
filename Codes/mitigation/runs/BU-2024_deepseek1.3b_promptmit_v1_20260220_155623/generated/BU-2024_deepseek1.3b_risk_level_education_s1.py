# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if obj.subject.history == 'clean' and obj.subject.assets >= 50000 and obj.subject.education == 'No Degree':
        return True
    else:
        return False

# Test the function
print(is_suitable(obj1))  # should return True
print(is_suitable(obj2))  # should return False
```

In the code above, `is_suitable` is a function that checks if an object (`obj`) is suitable. The function checks if the subject of the object is 'clean', if the assets are greater than or equal to 50000,