# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
    
    if (obj.history == 'clean' and obj.assets >= 50000 and obj.education == 'No Degree'):
        return True
    else:
        return False

# Use the function.

# Create an object:
company1 = Company('Apple', 'clean', 60000, 'Degree')
company2 = Company('Microsoft', 'dirty', 50000, 'No Degree')

print(is_suitable(company1)) # Returns: True
print(is_suitable(company2)) # Returns: False
```

In the code above, the `