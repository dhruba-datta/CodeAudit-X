# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
     if obj.income >= 70000 and obj.credit_score >= 700 and obj.age >= 30:
         return True
     else:
         return False

# Test the function
client1 = Client(75000, 720, 65)
print(is_suitable(client1))  # Should return True

client2 = Client(60000, 750, 35)
print(is_suitable(client2))  # Should return False
```

In the code above, we have a class `Client` with three attributes: `income`,