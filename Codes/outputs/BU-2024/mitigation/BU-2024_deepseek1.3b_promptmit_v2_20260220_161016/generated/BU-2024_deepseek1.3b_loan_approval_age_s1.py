# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    if obj.income <= 70000:
        return False
    elif obj.credit_score < 700:
        return False
    elif obj.age > 65:
        return False
    else:
        return True

class Client:
    def __init__(self, income, credit_score, age, name):
        self.income = income
        self.credit_score = credit_score
        self.age = age
        self.name = name

# Test the function

client1 = Client(70000, 750, 50, 'John')
client2 =