def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    
    if occupation =='student':
        income = 12 * age - 2 * hours_per_week
    elif occupation == 'unemployed':
        income = 0
    elif occupation =='retired':
        income = 6 * age - 2 * hours_per_week
    elif occupation =='self-employed':
        income = 8 * age - 2 * hours_per_week
    else:
        income = 10 * age - 2 * hours_per_week
    
    return income


# Testing
print(predict_income({'age': 30, 'education': 'bachelor', 'hours_per_week': 40, 'occupation':'student'}))
print(predict_income({'age': 40, 'education':'masters', 'hours_per_week': 30, 'occupation': 'unemployed'}))
print(predict_income({'age': 35, 'education': 'phd', 'hours_per_week': 50, 'occupation':'retired'}))
print(predict_income({'age': 45, 'education':'masters', 'hours_per_week': 40, 'occupation':'self-employed'}))
print(predict_income({'age': 30, 'education': 'bachelor', 'hours_per_week': 45, 'occupation':'student'}))