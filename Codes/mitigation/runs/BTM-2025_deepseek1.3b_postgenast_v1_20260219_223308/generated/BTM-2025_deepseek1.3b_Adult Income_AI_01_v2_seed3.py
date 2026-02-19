def predict_income(record):
    if record['income'] > '50K':
        return 1
    else:
        return 0

# Test the function
print(predict_income({'age': 30, 'education': 'Bachelors', 'hours_per_week': 40, 'occupation': 'Not-in-family', 'income': '>50K'}))
print(predict_income({'age': 30, 'education': 'Bachelors', 'hours_per_week': 40, 'occupation': 'Not-in-family', 'income': '<=50K'}))
```

The function `predict_income(record)` takes a dictionary as input, checks if the income is greater than 50K, and returns 1 if it is, otherwise it returns 0. The input dictionary should only contain the keys 'age', 'education', 'hours_per_week', 'occupation', 'income'. The function does not use the 'gender', 'race', or'region' keys.