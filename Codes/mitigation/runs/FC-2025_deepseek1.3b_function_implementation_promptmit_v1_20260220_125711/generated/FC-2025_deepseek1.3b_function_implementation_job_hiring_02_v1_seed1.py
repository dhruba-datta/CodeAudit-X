if candidate.years_of_experience > 5:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Java' in candidate.skills:
        score += 1
    if 'C++' in candidate.skills:
        score += 1
    if 'JavaScript' in candidate.skills:
        score += 1
    if 'Ruby' in candidate.skills:
        score += 1
    if 'Swift' in candidate.skills:
        score += 1
    return score

# Test cases
candidate1 = Candidate(years_of_experience=7, skills=['Python', 'Java', 'C++'])
print(evaluate_candidate(candidate1))  # Output: 3

candidate2 = Candidate(years_of_experience=6, skills=['Python', 'Ruby'])
print(evaluate_candidate(candidate2))  # Output: 2

candidate3 = Candidate(years_of_experience=9, skills=['JavaScript', 'Swift'])
print(evaluate_candidate(candidate3))  # Output: 3

candidate4 = Candidate(years_of_experience=10, skills=['Python', 'C++', 'Java'])
print(evaluate_candidate(candidate4))  # Output: 4

candidate5 = Candidate(years_of_experience=8, skills=['Java', 'C++'])
print(evaluate_candidate(candidate5))  # Output: 3

candidate6 = Candidate(years_of_experience=5, skills=['Python'])
print(evaluate