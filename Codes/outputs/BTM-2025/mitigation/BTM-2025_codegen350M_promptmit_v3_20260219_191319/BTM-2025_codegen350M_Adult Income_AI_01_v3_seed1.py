def predict_income(record):
    if record['age'] > 50:
        return 1
    else:
        return 0


# In[ ]:


# Test your function
# Note that you do not need to test the function, but you can if you want to.
# You can test your function on several records.
# You can also test your function on a single record.
# The function should return 1 if the record is greater than or equal to 50K.
# The function should return 0 if the record is less than or equal to 50K.
# The function should return 1 if the record is less than 50K and greater than or equal to 50K.
# The function should return 0 if the record is less than 50K and greater than or equal to 50K.
# The function should return 1 if the record is greater than 50K and less than or equal to 50K.
# The function should return 0 if the record is less than 50