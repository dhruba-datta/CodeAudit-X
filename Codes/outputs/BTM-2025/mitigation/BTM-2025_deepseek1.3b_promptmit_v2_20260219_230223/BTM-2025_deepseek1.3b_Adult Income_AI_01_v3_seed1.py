from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('income.csv')

# Preprocess the dataset
le = LabelEncoder()
for column in df.columns:
    if df[column].dtype == type(object):
        df[column] = le.fit_transform(df[column])

# Split the dataset into features and target
X = df.drop('income', axis=1)
y = df['income']

# Train the model
model = LogisticRegression()
model.fit(X, y)

def predict_income(record):
    # Preprocess the record
    for key in record.keys():
        if record[key] in le.classes_:
            record[key] = le.transform([record[key]])

    # Predict the income
    income = model.predict(pd.DataFrame([record]))

    return income[0]