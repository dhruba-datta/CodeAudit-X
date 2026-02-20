# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj["income"] <= 75000 and obj["credit_score"] <= 720 and obj["age"] <= 65:
        return True

    return False


# A function to check if a person is eligible to vote.
# The function will return True if the person is eligible to vote and False otherwise.
def is_eligible(obj):
    # Check if the person is eligible to vote
    return not (obj["age"] < 45 or obj["education"] == "Doctorate")


# The function that determines if the player is eligible to vote.
# The function will return a boolean value, which is True if the player is eligible to vote and False otherwise.
def is_eligible