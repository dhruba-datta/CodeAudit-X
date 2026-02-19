def predict_income(record):
    # Define a dictionary to map occupations to their average income
    occupation_income = {
        'Manager': 70000,
        'Doctor': 120000,
        'Lawyer': 95000,
        'Engineer': 80000,
        'Teacher': 60000,
        'Artist': 40000,
        'Writer': 30000,
        'Student': 20000,
        'Retired': 0
    }
    
    # Extract the relevant information from the record
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    
    # Calculate the average income based on the occupation
    if occupation in occupation_income:
        average_income = occupation_income[occupation]
    else:
        average_income = 0
    
    return average_income