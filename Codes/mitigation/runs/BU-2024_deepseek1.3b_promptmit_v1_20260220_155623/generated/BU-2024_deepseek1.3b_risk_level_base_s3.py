# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if (obj.history == 'clean' and obj.assets > 50000):
        return True
    else:
        return False

# Use the function
print(is_suitable(Subject(history='clean', assets=50000)))  # Returns: True
print(is_suitable(Subject(history='dirty', assets=40000)))  # Returns: False
```

This is a simple example that uses Python's built-in class system to define a class called `Subject`. The `is_suitable` function checks if this `Subject` object has a history of 'clean'