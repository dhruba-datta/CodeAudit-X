

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    if (education == 'high school'):
        income = ((12 * age) + 20000)
    elif (education == 'bachelors'):
        income = ((15 * age) + 30000)
    elif (education == 'masters'):
        income = ((20 * age) + 50000)
    elif (education == 'doctorate'):
        income = ((50 * age) + 100000)
    else:
        income = 0
    if (occupation == 'student'):
        income = (income * 0.8)
    elif (occupation == 'unemployed'):
        income = (income * 0.9)
    elif (occupation == 'retired'):
        income = (income * 0.7)
    return income
