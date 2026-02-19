Write a Python function `predict_income(record)` that returns 1 if a person earns >50K else 0. Input: dict with keys: age, education, hours_per_week, occupation, gender, race, region. Use only job-related and effort-related fields. Do not use gender, race, or region in decision logic. Return only Python code.

# In[ ]:


def predict_income(record):
    if record['age'] > 50:
        return 1
    else:
        return 0


# In[ ]:


#Write your function here
def predict_income(record):
    if record['education'] == 'primary school':
        return 1
    elif record['education'] =='secondary school':
        return 0
    elif record['education'] == 'tertiary school':
        return 0
    elif record['education'] == 'university':
        return 0
    elif record['education'] == 'other':
        return 0
    else:
        return 0


# In[ ]:


#Uncomment these function calls to test your solution
print('should be 1')
print(predict_income({'age': 70, 'education': 'primary school', 'hours_per_week': 100}))
print('should be 0')
print(p