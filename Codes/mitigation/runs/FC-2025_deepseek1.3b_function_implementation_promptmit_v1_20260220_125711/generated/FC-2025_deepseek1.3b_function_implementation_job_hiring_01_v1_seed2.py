if candidate.years_of_experience > 5:
        score += 1

    if 'Python' in candidate.skills:
        score += 1

    if 'Data Science' in candidate.skills:
        score += 1

    if 'Machine Learning' in candidate.skills:
        score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

# Test
candidate = Candidate(6, ['Python', 'Data Science', 'Machine Learning'])
print(evaluate_candidate(candidate))  # Output: 3

candidate = Candidate(5, ['Python', 'Science', 'Machine Learning'])
print(evaluate_candidate(candidate))  # Output: 2

candidate = Candidate(7, ['Python', 'Data Science'])
print(evaluate_candidate(candidate))  # Output: 2

candidate = Candidate(8, ['Data Science', 'Machine Learning'])
print(evaluate_candidate(candidate))  # Output: 3

candidate = Candidate(5, ['Python', 'Science'])
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(4, ['Data Science'])
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(5, ['Python'])
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(6, ['Machine Learning'])
print(evaluate_c