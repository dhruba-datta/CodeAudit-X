```python
def predict_income(record):
    age = record['age']
    education = record['education']
    hours_per_week = record['hours_per_week']
    occupation = record['occupation']
    gender = record['gender']
    race = record['race']
    region = record['region']
    
    if (age < 20 or age > 65) or (education not in ['Bachelors', 'Some-college', '11th', 'HS-grad', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', 'Preschool', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', '32nd', '33rd', '34th', '35th', '36th', '37th', '38th', '39th', '40th', '41st', '42nd', '43rd', '44th', '45th', '46th', '47th', '48th', '49th', '50th', '51st', '52nd', '53rd', '54th', '55th', '56th', '57th