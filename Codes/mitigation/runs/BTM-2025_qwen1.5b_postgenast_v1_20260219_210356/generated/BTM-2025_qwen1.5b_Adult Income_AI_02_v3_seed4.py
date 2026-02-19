

def predict_income(record):
    education_thresholds = {'High School': 25000, 'Bachelor’s Degree': 40000, 'Master’s Degree': 60000, 'PhD': 80000}
    occupation_thresholds = {'Software Engineer': 70000, 'Data Scientist': 90000, 'Manager': 110000, 'Salesperson': 130000}
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    if (education in education_thresholds):
        education_income = education_thresholds[education]
    else:
        education_income = 40000
    if (occupation in occupation_thresholds):
        occupation_income = occupation_thresholds[occupation]
    else:
        occupation_income = 70000
    total_income = (education_income + occupation_income)
    return total_income
