

def predict_income(record):
    avg_income = (((record['education'] * 3) + record['hours_per_week']) / 4)
    return int((avg_income > 50000))
