

def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    SCRUBBED_ID = 'SCRUBBED_ATTR'
    SCRUBBED_ID = 'SCRUBBED_ATTR'
    SCRUBBED_ID = 'SCRUBBED_ATTR'
    if (SCRUBBED_ID == 'male'):
        if (SCRUBBED_ID == 'white'):
            if (SCRUBBED_ID == 'northeast'):
                return 50
            else:
                return 75
        elif (SCRUBBED_ID == 'northeast'):
            return 70
        else:
            return 50
    elif (SCRUBBED_ID == 'white'):
        if (SCRUBBED_ID == 'northeast'):
            return 70
        else:
            return 150
    elif (SCRUBBED_ID == 'northeast'):
        return 100
    else:
        return 150
