# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    
    if (obj.income >= 70000 and obj.credit_score >= 750):
        return True
    else:
        return False

# Test the function

client1 = Client(income=75000, credit_score=720)
client2 = Client(income=60000, credit_score=700)

print(is_suitable(client1))  # Should print: True
print(is_suitable(client2))  # Should print: False
<jupyter>
<empty_output>
<jupyter>
<