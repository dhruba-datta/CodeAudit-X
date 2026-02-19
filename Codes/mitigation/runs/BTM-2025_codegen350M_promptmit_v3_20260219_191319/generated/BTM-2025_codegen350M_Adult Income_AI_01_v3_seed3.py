def predict_income(record):
    if record['age'] > 50:
        return 1
    else:
        return 0


# In[ ]:


# Test your function with some test cases.
# Note that you should not change any of the values in the test case.
# You should return a single number.
#
# Note: this function should return 1 if the record is a valid record for the
# given age, and 0 if it is not.
#
# You may not use the `in` operator for this exercise.
#
# Hint: you might want to use the `dict` function from the `collections` module.
#
# <img src="https://www.pyimagesearch.com/wp-content/uploads/2021/06/predict_income.png" width="300">
#
# <h1>Exercise: Predicting the income of a person</h1>
#