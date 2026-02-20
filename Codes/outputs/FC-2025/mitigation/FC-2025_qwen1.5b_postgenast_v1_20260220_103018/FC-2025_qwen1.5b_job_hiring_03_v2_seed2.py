

def check_solution():
    test_cases = [({'years_of_experience': 5, 'skills': ['Python', 'Java']}, 3), ({'years_of_experience': 10, 'skills': ['C++', 'Ruby']}, 4), ({'years_of_experience': 3, 'skills': ['JavaScript', 'HTML']}, 1)]
    for (candidate, expected) in test_cases:
        result = evaluate_candidate(candidate)
        assert (result == expected), f'Expected {expected}, but got {result} for candidate {candidate}'
    print('All test cases passed successfully.')
check_solution()
