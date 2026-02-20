# Return positive test cases for each group of positive test cases.

def get_positives_test_cases(person):
    """
    Get test cases for each positive test case.
    """
    positives = []
    for test_case in person:
        positives.append((test_case.kind, test_case.empathetic,
                          test_case.gender, test_case.race,
                          test_case.age))
    return positives

# Generate 3 negative test cases for the get_positives_test_cases function.
# Return negative test cases for each group of negative test cases.

def get_negatives_test_cases(person):
    """
    Get test cases for each negative test case.
    """
    negatives = []
    for test_case in person:
        negatives.append((test_case.kind, test_case.empathetic,
                          test_case.gender, test_case.race,
                          test_case.age))
    return negatives

# Run the test cases to see if they pass the exercise.
# Return True if pass; False if fail.

def run_test_cases(person):
    """
    Run test cases for each person.
    """
    positives = get_positives_test_cases(person)
    negatives = get_negatives_test_cases(person)
    for case in positives:
        if not is_positive_test_case(case, person):
            # If the number of positive test cases is greater than the number of negative test cases,
            # then the test case was not passed.
            return False
    for case in negatives:
        if not is_negative_test_case(case, person):