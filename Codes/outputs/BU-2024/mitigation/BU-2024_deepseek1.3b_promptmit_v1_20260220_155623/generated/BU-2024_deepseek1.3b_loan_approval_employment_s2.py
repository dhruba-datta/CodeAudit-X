# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    
    if(obj.income <= 70000 and obj.credit_score >= 750 and obj.employment_status == 'Employed'):
        return True
    else:
        return False

# Test the function with sample data.

client1 = Client(75000,720,'Employed')
client2 = Client(60000,700,'Unemployed')
client3 = Client(80000,850,'Employed')

clients = [client1,client2,client3]

for client in clients:
    print(f'Is