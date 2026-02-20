# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
     if obj.income >= 70000 and obj.credit_score >= 750:
        return True
     else:
         return False

# Instantiate the Client class with income and credit_score.
client1 = Client(75000, 720)

# Check if client1 is suitable.
is_suitable(client1)
<jupyter>
<empty_output>
<jupyter>
<jupyter>
<jupyter>
<jupyter>
<jupyter>
<jupyter>
<jupyter>