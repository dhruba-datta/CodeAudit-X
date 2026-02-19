

def predict_income(record):
    if (record['age'] < 30):
        if (record['education'] == 'High School'):
            return 50000
        elif (record['education'] == "Bachelor's"):
            return 70000
        else:
            return 90000
    elif ((record['age'] >= 30) and (record['age'] <= 45)):
        if (record['education'] == 'High School'):
            return 60000
        elif (record['education'] == "Bachelor's"):
            return 80000
        else:
            return 100000
    elif (record['education'] == 'High School'):
        return 70000
    elif (record['education'] == "Bachelor's"):
        return 90000
    else:
        return 110000
