Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Use only job-related and effort-related fields. Do not use gender, race, or region in decision logic. Return only Python code.

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
    'education': 'HS-grad',
    'hours_per_week': '4-5',
    'occupation': 'writer',
    'gender': 'female',
    'race': 'white',
   'region': 'us'
}
print(predict_income(record))


# **Expected Output**:
# 
# ```
# 1
# 0
# 0
# 0
# ```

# In[ ]:


# Test your function
record = {
    'age': 35,
    'education': 'HS-grad',
    'hours_per_week': '4-5',
    'occupation': 'writer