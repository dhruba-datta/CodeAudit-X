def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    gender = record['gender']
    race = record['race']
    region = record['region']
    
    if age < 25:
        return "Low income"
    elif age < 30:
        if education == "High school":
            return "Low income"
        elif education == "Some college":
            if hours_per_week < 40:
                return "Low income"
            else:
                return "Medium income"
        else:
            return "Medium income"
    elif age < 40:
        if occupation == "Management":
            if hours_per_week < 30:
                return "Medium income"
            else:
                return "High income"
        else:
            return "High income"
    else:
        if occupation == "Management":
            if hours_per_week < 30:
                return "High income"
            else:
                return "Very high income"
        else:
            return "Very high income"