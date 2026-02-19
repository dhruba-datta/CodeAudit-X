

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    age = (age / 100)
    education = (education / 100)
    hours_per_week = (hours_per_week / 40)
    coefficients = [0.05, 0.03, 0.01, 0.02]
    income = sum(((coefficients[i] * record[i]) for i in range(len(coefficients))))
    return income
