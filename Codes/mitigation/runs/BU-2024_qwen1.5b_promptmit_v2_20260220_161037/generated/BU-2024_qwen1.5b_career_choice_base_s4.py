# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj['major'] == 'Journalism' and 'Writing' in obj['skills']

# Test the function with provided data points
print(is_suitable({'major': 'Journalism','skills': ['Writing']}))  # Expected output: True
print(is_suitable({'major': 'Engineering','skills': ['Programming']}))  # Expected output: False
```

**Explanation**:
The function `is_suitable` takes an object `obj` as input, which represents a person's profile. It checks if the person has a major of 'Journalism' and if they have at least one skill related to writing (e.g., 'Writing'). If both conditions are met, the function returns `True`, indicating