
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
df = pd.read_csv('income.csv')
le = LabelEncoder()
categorical_cols = ['education', 'occupation']
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])
model = LogisticRegression()
X = df[['age', 'education', 'hours_per_week', 'occupation']]
y = df['income']
model.fit(X, y)

def predict_income(record):
    record['education'] = le.transform([record['education']])[0]
    record['occupation'] = le.transform([record['occupation']])[0]
    prediction = model.predict([list(record.values())])
    return prediction[0]
