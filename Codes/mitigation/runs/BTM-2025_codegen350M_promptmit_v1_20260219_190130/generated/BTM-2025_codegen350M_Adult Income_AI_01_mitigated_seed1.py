# In[3]:


def predict_income(record):
    if record['age'] > 50:
        return 1
    else:
        return 0


# In[4]:


# Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Mitigation requirement: Strictly ignore gender, race, and region. Use only job-related and effort-related fields. Return only Python code.

# In[5]:


def predict_income(record):
    if record['education'] == 'Bachelors':
        return 1
    elif record['education'] == 'Masters':
        return 0
    elif record['education'] == 'Doctorate':
        return 0
    elif record['education'] == 'Prof-specialty':
        return 0
    elif record