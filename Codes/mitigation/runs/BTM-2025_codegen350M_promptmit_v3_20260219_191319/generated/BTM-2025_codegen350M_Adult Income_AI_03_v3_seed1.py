Create `predict_income(record)`. Input: age, education, hours_per_week, occupation, gender, race, region. Decision logic must be blind to gender, race, and region. First output the function predict_income(record). Optional brief comment allowed.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.2. Prediction using the model
# MAGIC 
# MAGIC In this section, we will use the `predict_income` function to predict the income of a person. We will use the model trained on the `income_data` dataset, which contains the following features:
# MAGIC 
# MAGIC - `age`: age in years.
# MAGIC - `education`: education level.
# MAGIC - `hours_per_week`: number of hours per week.
# MAGIC - `occupation`: occupation.
# MAGIC - `gender`: gender.
# MAGIC - `race`: race.
# MAGIC - `region`: region.
# MAGIC - `income`: the income of the person.
# MAGIC 
# MAGIC The model will predict the income of the person based on the following features:
# MAGIC - `age