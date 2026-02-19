def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    gender = record['gender']
    race = record['race']
    region = record['region']

    if gender =='male':
        if occupation =='student':
            if age < 30:
                return '<30'
            elif age < 40:
                return '30-40'
            else:
                return '40-50'
        elif occupation == 'blue-collar':
            if hours_per_week < 40:
                return '<40'
            else:
                return '40-50'
        elif occupation == 'technician':
            if hours_per_week < 40:
                return '<40'
            else:
                return '40-50'
        elif occupation =='retired':
            if hours_per_week < 40:
                return '<40'
            else:
                return '40-50'
        else:
            if hours_per_week < 40:
                return '<40'
            else:
                return '40-50'
    else:
        if occupation =='student':
            if age < 30:
                return '<30'
            elif age < 40:
                return '30-40'
            else:
                return '40-50'
        elif occupation == 'blue-collar':
            if hours_per_week <