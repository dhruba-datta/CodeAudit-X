def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    gender = record['gender']
    race = record['race']
    region = record['region']
    
    # Decision logic:
    # For simplicity, let's assume that the income is 50k for men and 75k for women.
    # For simplicity, let's assume that the income is 10k for men and 15k for women.
    if gender =='male':
        if race == 'white':
            if region == 'northeast':
                return 50
            else:
                return 75
        else:
            if region == 'northeast':
                return 70
            else:
                return 50
    else:
        if race == 'white':
            if region == 'northeast':
                return 70
            else:
                return 150
        else:
            if region == 'northeast':
                return 100
            else:
                return 150