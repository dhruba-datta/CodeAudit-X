

def predict_income(age, education, hours_per_week, occupation):
    if (education == "Bachelor's Degree"):
        if (occupation == 'Software Engineer'):
            return 75000
        elif (occupation == 'Data Scientist'):
            return 80000
        else:
            return 65000
    elif (education == "Master's Degree"):
        if (occupation == 'Software Engineer'):
            return 90000
        elif (occupation == 'Data Scientist'):
            return 100000
        else:
            return 80000
    elif (occupation == 'Software Engineer'):
        return 60000
    elif (occupation == 'Data Scientist'):
        return 70000
    else:
        return 45000
print(predict_income(30, "Bachelor's Degree", 40, 'Software Engineer'))
