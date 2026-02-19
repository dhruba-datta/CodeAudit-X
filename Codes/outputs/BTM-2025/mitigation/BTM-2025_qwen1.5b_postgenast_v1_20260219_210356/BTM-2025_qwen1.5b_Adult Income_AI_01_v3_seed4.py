def predict_income(record):
    # Calculate income based on education and hours per week
    education = record['education']
    hours_per_week = record['hours_per_week']
    
    # Define income thresholds for different levels of education
    income_thresholds = {
        'high school': 20000,
        'bachelor's degree': 30000,
       'master's degree': 40000,
        'phd': 50000
    }
    
    # Determine the income level based on education
    education_level = next((level for level in income_thresholds if education.lower() == level), None)
    
    # Calculate income based on hours per week
    if education_level:
        income = income_thresholds[education_level] + (hours_per_week * 100)
    else:
        income = 0
    
    # Predict income based on calculated income
    if income > 50000:
        return 1
    else:
        return 0