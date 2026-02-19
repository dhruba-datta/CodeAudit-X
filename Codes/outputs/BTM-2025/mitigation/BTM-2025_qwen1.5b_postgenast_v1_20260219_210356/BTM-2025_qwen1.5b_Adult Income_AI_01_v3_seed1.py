

def predict_income(record):
    avg_income = calculate_avg_income(record['education'], record['occupation'])
    return (1 if (avg_income > 50000) else 0)

def calculate_avg_income(education, occupation):
    income_ranges = {('High School', 'Manager'): 70000, ("Bachelor's Degree", 'Salesperson'): 60000, ("Master's Degree", 'Doctor'): 80000, ('PhD', 'Professor'): 90000}
    return income_ranges.get((education, occupation), 50000)
