# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if(obj.income <= 70000):
        return False
    if(obj.credit_score < 750):
        return False
    return True

class Client:
    def __init__(self, income, credit_score):
        self.income = income
        self.credit_score = credit_score

# Create instances of Client
client1 = Client(75000, 720)
client2 = Client(65000, 700)
client3 = Client(80000, 800)

# Call the is_suitable function