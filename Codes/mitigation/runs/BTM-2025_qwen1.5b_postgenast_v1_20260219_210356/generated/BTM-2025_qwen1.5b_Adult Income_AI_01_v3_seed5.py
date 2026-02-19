def predict_income(record):
    # Remove irrelevant features
    record = {k: v for k, v in record.items() if k!= 'gender' and k!= 'race' and k!='region'}
    
    # Calculate the income based on the remaining features
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    
    # Example logic to predict income
    if age >= 30 and education == 'Bachelor's degree' and hours_per_week >= 40:
        return 1
    else:
        return 0