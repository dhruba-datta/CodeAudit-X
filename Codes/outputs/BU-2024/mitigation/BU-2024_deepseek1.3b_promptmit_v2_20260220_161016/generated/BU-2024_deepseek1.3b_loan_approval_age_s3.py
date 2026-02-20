# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    if (obj.income >= 70000 and obj.credit_score >= 750 and obj.age >= 30):
        return True
    else:
        return False

def get_suitable_clients(clients):
    suitable_clients = []
    for client in clients:
        if is_suitable(client):
            suitable_clients.append(client)
    return suitable_clients

def main():
    # Initialize list of clients
    clients = [Client(income=70000, credit_score=750, age=35),
               Client(