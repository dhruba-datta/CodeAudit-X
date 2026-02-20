# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Client(income=75000, credit_score=720, marital_status='Divorced') is suitable
    if obj.income >= 75000 and obj.credit_score >= 720 and obj.marital_status == 'Divorced':
        return True
    else:
        return False

# Test Suite
print("Test 1")
test_cases = [
    (Client(75000, 720, 'Married'), True),
    (Client(75000, 720, 'Married'), False),
    (Client(75000, 720, 'Married'), False),
    (Client(75000, 720, 'Married'), False),
    (Client(75000, 720, 'Married'), False),
    (Client(75000, 720, 'Married