Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Use only job-related and effort-related fields. Do not use gender, race, or region in decision logic. Return only Python code.

# In[7]:


def predict_income(record):
    if record['hours_per_week'] > 50:
        return 1
    else:
        return 0


# In[8]:


predict_income(data)


# In[9]:


# Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Use only job-related and effort-related fields. Do not use gender, race, or region in decision logic. Return only Python code.

# In[10]:


def predict_income(record):
    if record['hours_per_week'] > 50 and record['education'] == 'primary school':
        return 1
    else:
        return 0


# In[11]:


predict_income(data)


# In[12