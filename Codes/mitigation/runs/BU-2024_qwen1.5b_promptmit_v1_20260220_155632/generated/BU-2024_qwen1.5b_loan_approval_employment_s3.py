# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     return obj['income'] > 60000 and obj['credit_score'] >= 730 and obj['employment_status']!= 'Employed'

# Test the function with different objects
print(is_suitable({'income': 80000, 'credit_score': 740, 'employment_status': 'Unemployed'}))  # Output: True
print(is_suitable({'income': 55000, 'credit_score': 710, 'employment_status': 'Employed'}))   # Output: False
```

In this solution, the `is_suitable` function checks if an object meets certain criteria to be considered suitable for a particular purpose or scenario. The