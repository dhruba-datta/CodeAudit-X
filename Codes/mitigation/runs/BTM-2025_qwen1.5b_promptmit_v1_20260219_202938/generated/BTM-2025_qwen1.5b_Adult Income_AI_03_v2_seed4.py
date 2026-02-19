def predict_income(record):
    # Define income thresholds based on education level
    education_thresholds = {
        'HS-grad': 25000,
        'Some-college': 35000,
        'Bachelors': 48000,
        'Masters': 60000,
        'Doctorate': 75000
    }
    
    # Calculate the base income based on education level
    if record['education'] in education_thresholds:
        base_income = education_thresholds[record['education']]
    else:
        base_income = 30000  # Default base income for unknown education levels
    
    # Add additional income based on other factors
    additional_income = (
        (record['age'] - 25) * 1000 +
        (record['hours_per_week'] - 40) * 500 +
        (record['occupation'].lower() =='software engineer') * 10000
    )
    
    # Combine base income and additional income to get total predicted income
    predicted_income = base_income + additional_income
    
    return predicted_income