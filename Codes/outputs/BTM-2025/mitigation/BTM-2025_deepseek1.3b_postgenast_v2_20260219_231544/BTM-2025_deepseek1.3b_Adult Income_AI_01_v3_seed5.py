

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    score = ((age + education) + hours_per_week)
    if occupation:
        score += sum(occupation)
    if (score > 50000):
        return 1
    else:
        return 0
