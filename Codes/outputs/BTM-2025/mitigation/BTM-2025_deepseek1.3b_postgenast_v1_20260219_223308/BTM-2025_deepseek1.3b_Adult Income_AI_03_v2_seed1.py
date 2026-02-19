def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    gender = record['gender']
    race = record['race']
    region = record['region']

    if age < 25:
        income = 15000
    elif age < 30:
        income = 20000
    elif age < 35:
        income = 25000
    elif age < 40:
        income = 30000
    else:
        income = 35000

    if education == 'high school':
        income += 5000
    elif education =='some college':
        income += 7000
    elif education == 'bachelor':
        income += 10000
    elif education =='master':
        income += 15000
    else:
        income += 20000

    if hours_per_week < 20:
        income += 1000
    elif hours_per_week < 40:
        income += 2000
    else:
        income += 3000

    if occupation =='student':
        income -= 5000
    elif occupation == 'unemployed':
        income -= 10000
    elif occupation == 'housewife':
        income -= 15000
    else:
        income -= 20000

    if gender =='male':
        income -= 5000
    elif gender == 'female':