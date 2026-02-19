def predict_income(record):
    if record['age'] < 50:
        return 1
    else:
        return 0


# In[ ]:


# Test your function
record = {
    'age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'education': ['M', 'Bachelors', 'Masters', 'Prof-school', 'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate'],
    'hours_per_week': [4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],
    'occupation': ['Doctor', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school', 'Prof-school',