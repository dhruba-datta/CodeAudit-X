# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if(obj.skills == 'Data Scientist' and obj.income > 70000 and obj.credit_score > 700 ):
        return True
    else:
        return False

# Test the function with sample data.

client1 = Client(skills='Data Scientist', income=75000, credit_score=720)
client2 = Client(skills='Data Scientist', income=60000, credit_score=750)
client3 = Client(skills='Data Scientist', income=50000, credit_score=800