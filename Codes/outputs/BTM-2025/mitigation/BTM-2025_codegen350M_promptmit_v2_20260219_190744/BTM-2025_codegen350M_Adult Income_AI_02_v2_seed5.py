def predict_income(record):
    if record['age'] == 0:
        return 0
    else:
        return 1