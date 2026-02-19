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
    'education': 'Bachelors',
    'hours_per_week': 10,
    'occupation': 'Prof-specialist',
    'gender': 'Male',
    'race': 'White',
   'region': 'South Africa'
}
print(predict_income(record))


# In[7]:


# Exercise
# 1. Create a function called `predict_income_with_age_and_occupation()` that takes a dictionary `record` as input. The function should return 1 if a person earns >50K else 0.
# 2. Create a function called `predict_income_with_age_and_occupation()` that takes a