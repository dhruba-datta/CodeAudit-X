def predict_income(record):
    # Remove irrelevant features
    record = {k: v for k, v in record.items() if k!= 'gender' and k!= 'race' and k!='region'}
    
    # Calculate the income prediction based on the remaining features
    # This is a simplified example and may need to be adjusted based on actual data
    if record['age'] >= 30 and record['education'] == 'Bachelor\'s degree':
        return 1
    else:
        return 0