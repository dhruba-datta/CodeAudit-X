def predict_income(record):
    return record['education'] >= 12 and record['hours_per_week'] >= 40