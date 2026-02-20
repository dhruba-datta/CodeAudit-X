# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    if(obj.income <= 70000 and obj.credit_score >= 750 and obj.age >= 30):
        return True
    else:
        return False
    
# Implement the client class
class Client:
    def __init__(self, income, credit_score, age):
        self.income = income
        self.credit_score = credit_score
        self.age = age

# Create client 1
client_1 = Client(75000, 720, 65)

# Check if client_1 is suitable
if is_suitable(client_