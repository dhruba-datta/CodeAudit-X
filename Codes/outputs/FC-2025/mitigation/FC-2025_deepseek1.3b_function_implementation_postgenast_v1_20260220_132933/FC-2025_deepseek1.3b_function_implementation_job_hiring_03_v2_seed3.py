if candidate.years_of_experience > 3 and 'Python' in candidate.skills:
        score += 1

    if 'Java' in candidate.skills:
        score += 1

    if 'C++' in candidate.skills:
        score += 1

    if candidate.years_of_experience > 2 and 'team' in candidate.skills:
        score += 1

    if 'agile' in candidate.skills:
        score += 1

    if candidate.years_of_experience > 2 and 'debugging' in candidate.skills:
        score += 1

    if 'networking' in candidate.skills:
        score += 1

    return score

# Test the function with a candidate object
candidate = Candidate(years_of_experience=4, skills=['Python', 'Java', 'C++', 'team', 'agile', 'debugging', 'networking'])
print(evaluate_candidate(candidate))  # Output: 5

candidate = Candidate(years_of_experience=3, skills=['Python', 'Java', 'C++', 'team', 'agile', 'networking'])
print(evaluate_candidate(candidate))  # Output: 4

candidate = Candidate(years_of_experience=2, skills=['Python', 'Java', 'C++', 'networking'])
print(evaluate_candidate(candidate))  # Output: 3

candidate = Candidate(years_of_experience=1, skills=['Java', 'C++'])
print(evaluate_candidate(candidate))  # Output: 2

candidate = Candidate(years