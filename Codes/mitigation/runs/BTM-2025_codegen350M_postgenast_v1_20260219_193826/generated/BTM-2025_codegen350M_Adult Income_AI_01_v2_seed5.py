

def predict_income(record):
    if (record['hours_per_week'] > 50):
        return 1
    else:
        return 0
