# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if obj.income <= 70000 or obj.credit_score <= 650:
        return False # The client is not suitable
    else:
        return True # The client is suitable

# Sample usage
client1 = Client(income=70000, credit_score=750)
client2 = Client(income=50000, credit_score=700)

print(is_suitable(client1)) # False
print(is_suitable(client2)) # True

# Note: The decision logic above is a very simplistic version of a decision tree.
#