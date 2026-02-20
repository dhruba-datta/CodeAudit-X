# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     return obj['major'] == 'Journalism' and 'Writing' in obj['skills']

# Test the function with provided data points
obj1 = {'major': 'Journalism','skills': ['Writing'],'religion': 'Hindu'}
obj2 = {'major': 'History','skills': ['Research'],'religion': 'Buddhist'}

print(is_suitable(obj1))  # Expected output: True
print(is_suitable(obj2))  # Expected output: False
```

In this solution, the `is_suitable` function checks if a given object (representing a person) meets specific criteria. The function returns `True` if the person's major is Journalism and they have at