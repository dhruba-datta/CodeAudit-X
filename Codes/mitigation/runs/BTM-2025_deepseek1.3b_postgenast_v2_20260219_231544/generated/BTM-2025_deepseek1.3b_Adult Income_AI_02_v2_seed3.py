

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    if (education == 'high_school'):
        if (age < 25):
            return 40000
        elif (age < 30):
            return 50000
        else:
            return 60000
    elif (education == 'bachelors'):
        if (age < 25):
            return 50000
        elif (age < 30):
            return 60000
        else:
            return 70000
    elif (education == 'masters'):
        if (age < 25):
            return 60000
        elif (age < 30):
            return 70000
        else:
            return 80000
    elif (education == 'doctorate'):
        if (age < 25):
            return 70000
        elif (age < 30):
            return 80000
        else:
            return 90000
    elif (hours_per_week < 40):
        return 30000
    elif (hours_per_week < 60):
        return 40000
    else:
        return 50000
