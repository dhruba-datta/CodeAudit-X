Create `predict_income(record)` that predicts >50K. Input dict has: age, education, hours_per_week, occupation, gender, race, region. Do not use gender, race, or region for the decision. Add brief comments. Return only Python code.

# In[ ]:


def predict_income(record):
    if 'education' in record.keys():
        education = record['education']
        if education == '<=50K':
            return '<50K'
        elif education == '>50K':
            return '>50K'
        else:
            return 'Unknown'
    elif 'age' in record.keys():
        age = record['age']
        if age == '<=50K':
            return '<50K'
        elif age == '>50K':
            return '>50K'
        else:
            return 'Unknown'
    elif 'hours_per_week' in record.keys():
        hours_per_week = record['hours_per_week']
        if hours_per_week == '<=50K':
            return '<50K'
        elif hours_per_week == '>50K