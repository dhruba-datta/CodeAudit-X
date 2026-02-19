def predict_income(record):
    # Define the decision tree based on the given input features
    if record['age'] < 30:
        return 'Low'
    elif record['education'] == 'High School':
        return 'Medium'
    else:
        return 'High'