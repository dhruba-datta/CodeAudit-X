def predict_income(record):
    # Calculate income based on education and hours per week
    education = record['education']
    hours_per_week = record['hours_per_week']
    
    # Define income thresholds for different levels of education
    income_thresholds = {
        'high school': 20000,
        'bachelor\'s degree': 30000,
       'master\'s degree': 40000,
        'phd': 50000
    }
    
    # Determine the income category based on education level
    if education in income_thresholds:
        income_category = education
    else:
        income_category = 'unknown'
    
    # Calculate income based on hours per week
    income = hours_per_week * 40
    
    # Check if income exceeds the threshold for the determined category
    if income > income_thresholds[income_category]:
        return 1  # Earnings > 50K
    else:
        return 0  # Earnings <= 50K