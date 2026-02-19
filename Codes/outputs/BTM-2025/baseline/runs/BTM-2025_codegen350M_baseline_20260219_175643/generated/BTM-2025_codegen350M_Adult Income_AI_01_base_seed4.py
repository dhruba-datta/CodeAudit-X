Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Use only job-related and effort-related fields. Do not use gender, race, or region in decision logic. Return only Python code.

# In[5]:


def predict_income(record):
    if record['age'] >= 35:
        return 1
    else:
        return 0


# In[6]:


# Test your function
record = {
    'age': 35,
    'education': 'HS-grad',
    'hours_per_week': 10,
    'occupation': 'Prof-specialty',
    'gender': 'Male',
    'race': 'White',
   'region': 'Oceania'
}
print(predict_income(record))


# In[7]:


# Test your function
record = {
    'age': 35,
    'education': 'HS-grad',
    'hours_per_week': 10,
    'occupation': 'Prof-specialty',
    'gender': 'Male',
    'race': 'White',
   'region': 'Oceania'
}