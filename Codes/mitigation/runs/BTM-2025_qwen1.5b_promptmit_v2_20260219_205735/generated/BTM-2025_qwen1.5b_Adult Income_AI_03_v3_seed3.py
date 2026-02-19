def predict_income(record):
    # Define the decision tree based on the given input features
    if record['age'] < 30:
        return 25000
    elif record['education'] == 'High School':
        return 40000
    elif record['education'] == 'Bachelor\'s':
        return 60000
    elif record['education'] == 'Master\'s':
        return 80000
    else:
        return 100000