from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

# Assuming that the data is in a csv file named 'income.csv'
df = pd.read_csv('income.csv')

# Preprocess the data
le = LabelEncoder()

categorical_cols = ['education', 'occupation']
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Create the model
model = LogisticRegression()

# Prepare the data
X = df[['age', 'education', 'hours_per_week', 'occupation']]
y = df['income']

# Fit the model
model.fit(X, y)

def predict_income(record):
    # Preprocess the record
    record['education'] = le.transform([record['education']])[0]
    record['occupation'] = le.transform([record['occupation']])[0]
    
    # Predict
    prediction = model.predict([list(record.values())])
    
    return prediction[0]