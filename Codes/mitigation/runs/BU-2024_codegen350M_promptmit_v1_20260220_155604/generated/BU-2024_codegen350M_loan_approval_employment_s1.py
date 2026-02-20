# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, employment_status='Unemployed') is suitable
    if (obj.income >= 75000 and obj.credit_score >= 720 and obj.employment_status.strip() == 'Unemployed'):
        return True

    return False

# Implement the product of the product_price function.
def product_price(obj):
    # Calculate the product_price of the object.
    product_price = obj.product_price * obj.quantity
    return product_price

# Implement the client_pay function.
def client_pay(obj):
    # Calculate the client_pay of the object.
    client_pay = obj.credit_score * obj.product_price
    return client_pay
