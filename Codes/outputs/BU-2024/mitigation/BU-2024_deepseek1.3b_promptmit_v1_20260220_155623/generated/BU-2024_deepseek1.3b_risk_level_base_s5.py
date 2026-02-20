# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if obj.subject.history == 'clean':
        if obj.subject.assets >= 50000:
            return True
    return False

# Use the function
print(is_suitable(obj1))  # Output: True
print(is_suitable(obj2))  # Output: False
print(is_suitable(obj3))  # Output: False
```

This function checks if the object `obj` is suitable or not. The `obj` must have a subject attribute with a history attribute of 'clean' and assets attribute of at least 50000. If these conditions are met, the function returns True