# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, age=65) is suitable
    if obj <= 75000:
        return False
    elif 720 <= obj < 7200:
        return False
    elif 65 <= obj < 65000:
        return False
    elif obj >= 65000:
        return True
    else:
        print("Incorrect Objective Value")
        return False


def get_objective(obj, skills, income, history):
    # Get Objective based on Skills, Income and History
    if skills == 'credit_score':
        if income == 'income':
            if history == 'history':
                return -math.log(obj, 10)
            elif history =='skills':
                return -