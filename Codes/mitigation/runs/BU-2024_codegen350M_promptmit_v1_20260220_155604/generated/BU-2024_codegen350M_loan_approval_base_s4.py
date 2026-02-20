# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    if obj.income >= 75000 and obj.credit_score >= 720:
        return True
    else:
        return False

# Implement the check for the customer to pay a certain amount of money. Return a boolean.
def customer_pay(obj, amnt):
    if obj.income - amnt < 0:
        return False
    else:
        return True

# Implement the check for the customer to pay a certain amount of money. Return a boolean.
def customer_pay_with_credit(obj, amnt):
    if obj.income - amnt < 0:
        return False
    else:
        return True

# Implement the check