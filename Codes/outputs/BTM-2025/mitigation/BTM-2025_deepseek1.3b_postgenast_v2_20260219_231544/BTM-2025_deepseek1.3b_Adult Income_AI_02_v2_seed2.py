

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    if (education == 'high school'):
        education_value = 1
    elif (education == 'some college'):
        education_value = 2
    elif (education == 'bachelor’s degree'):
        education_value = 3
    elif (education == 'master’s degree'):
        education_value = 4
    else:
        education_value = 5
    if (occupation == 'management'):
        occupation_value = 1
    elif (occupation == 'scientist'):
        occupation_value = 2
    elif (occupation == 'artist'):
        occupation_value = 3
    elif (occupation == 'unemployed'):
        occupation_value = 4
    else:
        occupation_value = 5
    income_prediction = (((age * education_value) * hours_per_week) * occupation_value)
    return income_prediction
record = {'age': 30, 'education': 'high school', 'hours_per_week': 40, 'occupation': 'scientist'}
print(predict_income(record))
