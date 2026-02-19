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
    elif record['education'] == 'university':
        return 0
    elif record['education'] == 'other':
        return 0
    else:
        return 0


# In[ ]:


#Test your function
record = {
    'age': 23,
    'education': 'primary school',
    'hours_per_week': 4,
    'occupation': 'worker',
    'gender': 'female',
   'region':'south america'
}
print(predict_income(record))