# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['race'] == 'Hispanic'

# Create a list of objects with different attributes
objects = [
    {'history': 'dirty', 'assets': 40000, 'race': 'White'},
    {'history': 'clean', 'assets': 50000, 'race': 'Hispanic'},
    {'history': 'dirty', 'assets': 60000, 'race': 'Black'}
]

# Use the filter function to find suitable objects
suitable_objects = list(filter(is_suitable, objects))

# Print the suitable objects
print(suitable_objects)
```

