def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']

    if occupation =='skilled':
        occupation = 3
    elif occupation == 'unskilled':
        occupation = 2
    else:
        occupation = 1

    score = age + education + hours_per_week + occupation

    if score > 50000:
        return 1
    else:
        return 0