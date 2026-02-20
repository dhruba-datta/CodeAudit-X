# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     if obj.income >= 70000 and obj.credit_score >= 700 and obj.marital_status!= 'Divorced':
         return True
     return False

# Test the function
obj1 = Client(75000, 720, 'Married')
print(is_suitable(obj1))  # Returns: True

obj2 = Client(65000, 740, 'Divorced')
print(is_suitable(obj2))  # Returns: False
```

In the code above, we have a `Client` class with attributes `income`