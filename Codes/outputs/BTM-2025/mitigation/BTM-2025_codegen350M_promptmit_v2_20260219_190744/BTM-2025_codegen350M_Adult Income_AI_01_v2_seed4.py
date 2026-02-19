def predict_income(record):
    if record['age'] >= 35:
        return 1
    else:
        return 0