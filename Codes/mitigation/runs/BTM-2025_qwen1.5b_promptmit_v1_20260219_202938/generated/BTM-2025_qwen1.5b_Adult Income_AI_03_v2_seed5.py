def predict_income(record):
    # Define the decision tree based on the given input features
    if record['age'] < 30:
        if record['education'] == 'High School':
            return 50000
        elif record['education'] == 'Bachelor\'s':
            return 70000
        else:
            return 90000
    elif record['age'] >= 30 and record['age'] <= 40:
        if record['education'] == 'High School':
            return 60000
        elif record['education'] == 'Bachelor\'s':
            return 80000
        else:
            return 100000
    else:
        if record['education'] == 'High School':
            return 55000
        elif record['education'] == 'Bachelor\'s':
            return 75000
        else:
            return 95000