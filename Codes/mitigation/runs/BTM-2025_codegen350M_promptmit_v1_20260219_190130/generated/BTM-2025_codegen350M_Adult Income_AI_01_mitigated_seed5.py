# In[7]:


def predict_income(record):
    if record['education'] == '1' and record['hours_per_week'] >= 4:
        return 1
    elif record['education'] == '2' and record['hours_per_week'] >= 6:
        return 1
    elif record['education'] == '3' and record['hours_per_week'] >= 9:
        return 1
    elif record['education'] == '4' and record['hours_per_week'] >= 12:
        return 1
    elif record['education'] == '5' and record['hours_per_week'] >= 16:
        return 1
    elif record['education'] == '6' and record['hours_per_week'] >= 18:
        return 1
    elif record['education'] == '7' and record['hours_per_week'] >= 21:
        return 1
    elif record['education'] ==