Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere in the code or comments. Return only code.

# In[ ]:


class PredictIncome(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.predict(X)


# In[ ]:


# Create a predictor
predictor = PredictIncome()

# Create a pipeline
pipeline = Pipeline(steps=[('predictor', predictor)])

# Create a DataFrame
df = DataFrame(pipeline.fit_transform(X))

# Create the model
model = RandomForestRegressor()

# Create the grid search
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='neg_mean_absolute_error')

# Fit the grid search to the data
grid_search.fit(