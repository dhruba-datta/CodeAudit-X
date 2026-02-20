# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income < 0 or obj.credit_score < 0 or obj.marital_status == 'Married':
        return False
    return True

# Implement the card_set_check function. Return a boolean.
def is_card_set(obj):
    # Check if obj is in card_set
    return obj in card_set

# Implement the card_set_score_check function. Return a boolean.
def card_set_score_check(obj):
    # Check if obj is in card_set_score
    if obj in card_set_score:
        return True
    return False

# Implement the card_set_