# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
     return obj.income > 60000 and obj.credit_score >= 740 and obj.marital_status!= 'Married'

# Create an instance of Client
client = Client(income=75000, credit_score=720, marital_status='Divorced')

# Call the is_suitable function with the client object as an argument
result = is_suitable(client)

# Print the result
print(result)  # Output: True

# Define a new class Client with additional attributes
class Client:
    def __init__(self, income, credit_score, marital_status, age):
        self.income = income
        self.credit_score = credit_score
        self.marital_status =