# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
     if obj.income >= 70000 and obj.credit_score >= 700 and obj.employment_status == 'Employed':
        return True
     else:
        return False

# Create a list of potential clients
clients = [Client(income=72000, credit_score=750, employment_status='Employed'),
           Client(income=68000, credit_score=700, employment_status='Unemployed'),
           Client(income=76000, credit_score=800, employment_status='Employed'),
          