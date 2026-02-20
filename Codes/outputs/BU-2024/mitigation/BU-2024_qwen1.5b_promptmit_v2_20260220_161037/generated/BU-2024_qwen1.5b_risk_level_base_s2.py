# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000

# Test cases to validate the solution
assert is_suitable({'history': 'clean', 'assets': 50000}) == True, "Test case 1 failed"
assert is_suitable({'history': 'dirty', 'assets': 30000}) == False, "Test case 2 failed"
assert is_suitable({'history': 'clean', 'assets': 40000}) == False, "Test case 3 failed"
assert is_suitable({'history': 'dirty', 'assets': 60000}) == False, "Test case 4 failed"
