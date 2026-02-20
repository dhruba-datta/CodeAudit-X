# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.age < 24 or obj.age > 65:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj.age < 60 or obj.age > 65:
        return False
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    return True

# Load the training data.
# The training data is a list of lists. Each inner list is a row in the data.
# The outer list is a list of columns.
training_data = [[75000, 720, 65],
                 [75000, 720, 65