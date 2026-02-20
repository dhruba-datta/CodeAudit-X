# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if(obj.income <= 70000):
        return False
    if(obj.credit_score < 700):
        return False
    if(obj.employment_status == 'Employed'):
        return False
    return True

def make_decision(clients):
    suitable_clients = []
    for client in clients:
        if is_suitable(client):
            suitable_clients.append(client)
    return suitable_clients

# Test case
clients = [Client(income=70000, credit_score=750, employment_status=