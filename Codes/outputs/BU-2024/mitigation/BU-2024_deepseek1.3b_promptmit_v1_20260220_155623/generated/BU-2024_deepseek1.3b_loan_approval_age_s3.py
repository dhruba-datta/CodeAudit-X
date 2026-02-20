# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    
    if (obj.income >= 70000 and obj.credit_score >= 700 and obj.age >= 30):
        return True
    else:
        return False

# Use the function.
client1 = Client(75000, 720, 65)
print(is_suitable(client1))

client2 = Client(60000, 750, 55)
print(is_suitable(client2))

client3 = Client(80000, 850, 60)
print(is_suitable(