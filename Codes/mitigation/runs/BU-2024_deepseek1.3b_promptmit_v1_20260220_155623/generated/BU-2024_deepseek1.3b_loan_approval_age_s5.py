# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    suitable = False

    if obj.income >= 70000 and obj.credit_score >= 700 and obj.age <= 60:
        suitable = True

    return suitable

# Test the function with some data.
# Data should be a list of objects, each of which is a Client instance.
data = [
    Client(income=75000, credit_score=720, age=65),
    Client(income=60000, credit_score=750, age=55),
    Client(income=70000, credit_score=8