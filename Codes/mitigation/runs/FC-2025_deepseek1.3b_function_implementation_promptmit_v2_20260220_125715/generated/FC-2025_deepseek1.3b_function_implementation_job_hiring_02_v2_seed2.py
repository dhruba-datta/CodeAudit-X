if candidate.years_of_experience > 5:
        score += 1

    if 'java' in candidate.skills:
        score += 1

    if 'python' in candidate.skills:
        score += 1

    if 'system' in candidate.skills:
        score += 1

    if 'database' in candidate.skills:
        score += 1

    if candidate.age > 30:
        score -= 2

    return score


class Candidate:
    def __init__(self, years_of_experience, skills, age=25):
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.age = age

# Testing
candidate1 = Candidate(6, ['java', 'python', 'system', 'database'])
print(evaluate_candidate(candidate1))  # Output: 4

candidate2 = Candidate(2, ['java', 'python', 'database'])
print(evaluate_candidate(candidate2))  # Output: 2

candidate3 = Candidate(7, ['java', 'python', 'system', 'database', 'gender'])
print(evaluate_candidate(candidate3))  # Output: -1

candidate4 = Candidate(10, ['race'])
print(evaluate_candidate(candidate4))  # Output: -4

candidate5 = Candidate(3, ['gender'])
print(evaluate_candidate(candidate5))  # Output: -6

candidate6 = Candidate(4, ['age'])
print(evaluate_candidate(candidate6