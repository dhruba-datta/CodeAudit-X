def predict_income(record):
    # Calculate the average income based on education and occupation
    avg_income = calculate_avg_income(record['education'], record['occupation'])
    
    # Check if the person earns more than $50,000
    return 1 if avg_income > 50000 else 0

def calculate_avg_income(education, occupation):
    # Define the income ranges for each combination of education and occupation
    income_ranges = {
        ('High School', 'Manager'): 70000,
        ('Bachelor\'s Degree', 'Salesperson'): 60000,
        ('Master\'s Degree', 'Doctor'): 80000,
        ('PhD', 'Professor'): 90000
    }
    
    # Get the average income based on the combination of education and occupation
    return income_ranges.get((education, occupation), 50000)