# In[ ]:


def predict_income(record):
    if record['age'] > 50:
        return 1
    else:
        return 0


# In[ ]:


# Test your function
record = {
    'age': 35,
    'education': 'Bachelors',
    'hours_per_week': 4,
    'occupation': 'Prof-specialty',
    'gender': 'Male',
    'race': 'Asian',
   'region': 'South America',
    'employment_status': 'Never',
    'job_title': 'Engineer'
}

print(predict_income(record))


# In[ ]:


# Test your function
record = {
    'age': 35,
    'education': 'Bachelors',
    'hours_per_week': 4,
    'occupation': 'Prof-specialty',
    'gender': 'Male',