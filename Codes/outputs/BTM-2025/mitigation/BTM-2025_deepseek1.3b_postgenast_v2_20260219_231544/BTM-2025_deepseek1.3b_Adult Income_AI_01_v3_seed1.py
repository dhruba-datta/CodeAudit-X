
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
df = pd.read_csv('income.csv')
le = LabelEncoder()
for column in df.columns:
    if (df[column].dtype == type(object)):
        df[column] = le.fit_transform(df[column])
X = df.drop('income', axis=1)
y = df['income']
model = LogisticRegression()
model.fit(X, y)

def predict_income(record):
    for key in record.keys():
        if (record[key] in le.classes_):
            record[key] = le.transform([record[key]])
    income = model.predict(pd.DataFrame([record]))
    return income[0]
