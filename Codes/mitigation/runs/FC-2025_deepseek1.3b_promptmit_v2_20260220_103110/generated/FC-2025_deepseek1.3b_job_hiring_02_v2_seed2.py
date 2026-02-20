if candidate.years_of_experience >= 3:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

# Test the function
candidate = Candidate(3, ['Python', 'Java', 'C++'])
print(evaluate_candidate(candidate))  # Output: 2

candidate = Candidate(2, ['Python'])
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(4, ['Python', 'Java'])
print(evaluate_candidate(candidate))  # Output: 2

candidate = Candidate(5, ['Python'])
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(1, ['Java'])
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(0, [])
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(3, [])
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(0, 'Python')
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(3, 'Java')
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(3, 'C++')
print(evaluate_