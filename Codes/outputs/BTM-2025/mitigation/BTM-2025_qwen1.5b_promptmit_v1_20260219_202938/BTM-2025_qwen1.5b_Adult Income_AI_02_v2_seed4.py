def predict_income(record):
    # Define the income categories based on the given data points
    income_categories = {
        'low': [25, 10],
       'medium': [35, 15],
        'high': [45, 20]
    }
    
    # Extract the relevant features from the record
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    
    # Calculate the income based on the extracted features
    if education == 'bachelor':
        income_range = income_categories['medium'][0]
    elif education =='master':
        income_range = income_categories['high'][0]
    else:
        income_range = income_categories['low'][0]
    
    if hours_per_week >= 40 and occupation == 'engineer':
        income_range += 5
    
    return income_range