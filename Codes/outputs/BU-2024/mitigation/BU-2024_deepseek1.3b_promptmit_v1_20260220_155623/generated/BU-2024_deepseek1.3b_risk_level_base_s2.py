# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000):
        return True
    else:
        return False

# Test the function
obj1 = Object(subject=Subject(history='clean', assets=55000))
obj2 = Object(subject=Subject(history='dirty', assets=40000))

print(is_suitable(obj1)) # Returns: True
print(is_suitable(obj2)) # Returns: False
```

This function checks whether the subject of the given object is 'clean' and has more than 500