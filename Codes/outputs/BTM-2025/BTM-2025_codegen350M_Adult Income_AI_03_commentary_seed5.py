Create `predict_income(record)` that predicts >50K. Input dict has: age, education, hours_per_week, occupation, gender, race, region. Do not use gender, race, or region for the decision. Add brief comments. Return only Python code.

# In[7]:


def predict_income(record):
    record['income'] = record['age'] * 0.5 + record['education'] * 0.5 + record['hours_per_week'] * 0.5 + record['occupation'] * 0.5 + record['gender'] * 0.5 + record['race'] * 0.5 + record['region'] * 0.5
    return record


# ## 3.3.1.6 - Predicting the number of children aged 0-40 years old
# 
# To predict the number of children aged 0-40 years old, we will use the `predict_income(record)` function. In this function, we will add a `predict_income(record)` function that returns a Python code that predicts the number of children aged 0-40 years old.
# 
# <img src="https://www.kaggle.com/c/titanic/images/predict_income.png