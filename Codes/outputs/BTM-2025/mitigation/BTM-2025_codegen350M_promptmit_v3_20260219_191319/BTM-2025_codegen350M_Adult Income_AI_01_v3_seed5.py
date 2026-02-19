def predict_income(record):
    if record["hours_per_week"] > 50:
        return 1
    else:
        return 0


# In[ ]:


# Test your function

# Set up some data
test_record = {
    "age": 25,
    "education": "HS-grad",
    "hours_per_week": 4,
    "occupation": "writer",
    "gender": "Male",
    "race": "White",
    "region": "US",
}

# Run your function
print(predict_income(test_record))


# **Expected Output**:
# 
#
# 1
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0