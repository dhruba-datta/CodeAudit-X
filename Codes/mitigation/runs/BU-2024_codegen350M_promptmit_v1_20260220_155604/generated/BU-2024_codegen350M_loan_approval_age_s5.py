# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    # for the suitability check.
    # Check if the income is less than the credit score
    # Check if the age is less than 70
    if obj.income < obj.credit_score:
        return False
    elif obj.age < 70:
        return False
    else:
        return True

# Implement the card_suitability_check function.
def card_suitability_check(obj):
    # Check the suitability of the card.
    # Return a boolean.
    if is_suitable(obj):
        # Return True if the card is suitable
        return True
    else:
        # Return False if the card is