def predict_income(record):
  
  # Define variables
  age = record['age']
  education = record['education']
  hours_per_week = record['hours_per_week']
  occupation = record['occupation']
  gender = record['gender']
  race = record['race']
  region = record['region']
  
  # Create a dictionary containing the variables
  predict_dict = {'age':age, 'education':education, 'hours_per_week':hours_per_week, 'occupation':occupation, 'gender':gender, 'race':race,'region':region}
  
  # Create the decision logic
  decision_logic = {'age':predict_age(age), 'education':predict_education(education), 'hours_per_week':predict_hours_per_week(hours_per_week), 'occupation':predict_occupation(occupation),