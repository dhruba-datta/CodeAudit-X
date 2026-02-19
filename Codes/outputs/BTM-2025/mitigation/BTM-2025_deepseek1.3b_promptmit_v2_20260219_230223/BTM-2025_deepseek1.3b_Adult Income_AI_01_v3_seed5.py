def predict_income(record):
    # Assuming the input record is a dictionary with keys: age, education, hours_per_week, occupation
    # The values for age, education, hours_per_week, and occupation are integers
    # The value for occupation is a list of integers

    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']

    # Scoring model using age, education, hours_per_week, and occupation
    score = age + education + hours_per_week
    if occupation:
        score += sum(occupation)

    # Predicting income
    if score > 50000:
        return 1
    else:
        return 0