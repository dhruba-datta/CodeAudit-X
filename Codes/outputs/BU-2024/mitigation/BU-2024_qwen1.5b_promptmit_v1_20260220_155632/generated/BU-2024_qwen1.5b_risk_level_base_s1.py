# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj.history == 'clean' and obj.assets >= 50000

# Test the function with the given data points
assert is_suitable(Subject(history='clean', assets=50000)) == True, "Test case 1 failed"
assert is_suitable(Subject(history='dirty', assets=49999)) == False, "Test case 2 failed"
assert is_suitable(Subject(history='clean', assets=60000)) == False, "Test case 3 failed"

print("All test cases passed!")
```

In this solution, we define a `Subject` class with attributes `history` and `assets`. The `is_suitable` function checks if