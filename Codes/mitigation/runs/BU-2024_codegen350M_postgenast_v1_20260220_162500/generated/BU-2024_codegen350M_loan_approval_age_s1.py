def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if (obj.income >= 75000 and obj.credit_score >= 720 and obj.age >= 65):
        return True
    else:
        return False


def main():
    # Create a client object
    client = Client(income=75000, credit_score=720, age=65)

    # Get the client's name
    client_name = client.name

    # Check if a suitable client is returned
    if is_suitable(client):
        print("A suitable client is returned!")
    else:
        print("A suitable client is not returned!")

