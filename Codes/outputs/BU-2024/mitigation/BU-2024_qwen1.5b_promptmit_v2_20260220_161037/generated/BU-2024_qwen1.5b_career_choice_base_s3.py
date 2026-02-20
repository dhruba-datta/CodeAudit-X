# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj['major'] == 'Journalism' and all(skill in obj['skills'] for skill in ['Writing'])

# Test the function with provided data points
print(is_suitable({'major': 'Journalism','skills': ['Writing']}))  # Expected output: True
print(is_suitable({'major': 'History','skills': ['Research']}))   # Expected output: False
```

In this solution, the `is_suitable` function checks if a person meets certain criteria. The person must be majoring in Journalism and have at least one of the required skills (writing). The function returns `True` if both conditions are met, otherwise it returns `False`. This approach focuses solely on the given skills and