# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if obj.income > 75000 and obj.credit_score > 720:
        return True
    else:
        return False


class Client:
    def __init__(self, income, credit_score):
        self.income = income
        self.credit_score = credit_score

clients = [Client(73000, 75000), Client(68000, 70000), Client(80000, 78000)]

for client in clients:
    print(f"Client is suitable: {is_suit