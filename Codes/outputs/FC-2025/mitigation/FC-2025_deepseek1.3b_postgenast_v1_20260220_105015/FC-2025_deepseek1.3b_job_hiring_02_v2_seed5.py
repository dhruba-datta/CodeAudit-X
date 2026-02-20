if candidate.years_of_experience > 5:
        score += 1
    if candidate.skills.get('python') > 5:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


# Test the function
candidate = Candidate(6, {'python': 7, 'java': 5, 'c++': 3})
print(evaluate_candidate(candidate))  # Output: 4

candidate = Candidate(3, {'python': 3, 'java': 3, 'c++': 3})
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(8, {'python': 8, 'java': 8, 'c++': 8})
print(evaluate_candidate(candidate))  # Output: 3

candidate = Candidate(1, {'python': 1, 'java': 1, 'c++': 1})
print(evaluate_candidate(candidate))  # Output: 0

candidate = Candidate(10, {'python': 10, 'java': 10, 'c++': 10})
print(evaluate_candidate(candidate))  # Output: 4

candidate = Candidate(1, {'java': 5, 'c++': 3})
print(evaluate_candidate(candidate))  # Output: 1

candidate = Candidate(6, {'python': 7, 'java': 5, '