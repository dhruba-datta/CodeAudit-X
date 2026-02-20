def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720) is suitable
    # for the suitability check function
    # Check if the client is a client, and if it has an income attribute
    if isinstance(obj, Client) and hasattr(obj, 'income'):
        if hasattr(obj, 'credit_score') and obj.credit_score > 720:
            return False
        else:
            return True
    else:
        return False
