Create `predict_income(record)` to predict >50K. Input dict has: age, education, hours_per_week, occupation, gender, race, region. Decision logic must be blind to gender, race, and region. Include brief comments explaining the logic. Return only Python code.

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
        if age < 18:
            return '<18'
        elif age < 65:
            return '>65'
        elif age < 85:
            return '>85'
        else:
            return 'Unknown'
    elif 'hours_per_week' in record.keys():
        hours_per_week = record['hours_per_week']
        if hours_per_week < 25:
            return '>25'
        elif hours_per_week < 50: