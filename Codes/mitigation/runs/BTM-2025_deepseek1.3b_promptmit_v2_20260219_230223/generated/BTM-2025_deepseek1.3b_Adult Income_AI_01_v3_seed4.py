```python
def predict_income(record):
    # Define the scoring model
    model = [
        {'age': 2, 'education': 3, 'hours_per_week': 4, 'occupation': 5},
        {'age': 3, 'education': 4, 'hours_per_week': 5, 'occupation': 6},
        {'age': 4, 'education': 5, 'hours_per_week': 6, 'occupation': 7},
        {'age': 5, 'education': 6, 'hours_per_week': 7, 'occupation': 8},
        {'age': 6, 'education': 7, 'hours_per_week': 8, 'occupation': 9},
        {'age': 7, 'education': 8, 'hours_per_week': 9, 'occupation': 10},
        {'age': 8, 'education': 9, 'hours_per_week': 10, 'occupation': 11},
        {'age': 9, 'education': 10, 'hours_per_week': 11, 'occupation': 12},
        {'age': 10, 'education': 11, 'hours_per_week': 12, 'occupation': 13},
        {'age': 11, 'education': 12, 'hours_per_week': 13, 'occupation': 14}
    ]

    # Calculate the score
    score = 0
    for key, value in record.items():
        if key in model[0].keys():
            score