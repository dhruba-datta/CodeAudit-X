def predict_income(record):
    # Calculate the average income based on education level and hours per week
    avg_income = (record['education'] * 3 + record['hours_per_week']) / 4
    
    # Determine if the person earns more than $50K
    return int(avg_income > 50000)