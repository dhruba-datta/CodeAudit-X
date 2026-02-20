# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     if obj.income >= 70000 and obj.credit_score >= 750:
        return True
     else:
         return False

class Client:
    def __init__(self, income, credit_score):
        self.income = income
        self.credit_score = credit_score

# Create a Client object
c = Client(75000, 720)

# Call the function is_suitable
print(is_suitable(c)) # Should print True

# Modify the income and credit_score, and check again
c.income = 80000
