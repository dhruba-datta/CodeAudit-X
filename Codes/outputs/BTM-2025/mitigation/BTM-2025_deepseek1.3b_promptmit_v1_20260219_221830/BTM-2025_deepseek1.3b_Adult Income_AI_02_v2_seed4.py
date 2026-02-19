def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    
    # Assume the data is already normalized
    age = age / 100
    education = education / 100
    hours_per_week = hours_per_week / 40
    
    # Assume the model is a linear regression model
    # coefficients are assumed to be [age, education, hours_per_week, occupation]
    coefficients = [0.05, 0.03, 0.01, 0.02]
    
    income = sum(coefficients[i] * record[i] for i in range(len(coefficients)))
    
    return income