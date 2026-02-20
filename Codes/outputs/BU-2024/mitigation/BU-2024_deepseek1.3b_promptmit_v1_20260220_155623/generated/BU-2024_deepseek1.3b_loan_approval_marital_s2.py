# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    
    if(obj.income <= 70000 and obj.credit_score >= 750 and obj.marital_status!= 'Married'):
        return True
    else:
        return False


# Define the class
class Client:
    def __init__(self, income, credit_score, marital_status):
        self.income = income
        self.credit_score = credit_score
        self.marital_status = marital_status

# Create the object
client1 = Client(75000, 720, 'Divorced')

# Call the function
print