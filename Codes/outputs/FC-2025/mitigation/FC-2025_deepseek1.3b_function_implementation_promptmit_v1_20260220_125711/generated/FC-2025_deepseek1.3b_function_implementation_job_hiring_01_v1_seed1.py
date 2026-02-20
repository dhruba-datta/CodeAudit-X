# Years of experience
    if candidate.years_of_experience > 5:
        score += 5

    # Skills
    for skill in candidate.skills:
        if skill in ['Python', 'Java', 'C#', 'JavaScript']:
            score += 1
        elif skill in ['SQL', 'NoSQL', 'Oracle', 'MongoDB']:
            score += 2
        elif skill in ['AWS', 'Azure', 'GCP', 'AKS', 'Kubernetes']:
            score += 3

    return score


class Candidate:

    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

# Test
candidate = Candidate(6, ['Python', 'SQL', 'GCP', 'Kubernetes'])
assert evaluate_candidate(candidate) == 10

candidate = Candidate(5, ['Java', 'AWS', 'NoSQL'])
assert evaluate_candidate(candidate) == 8

candidate = Candidate(10, ['JavaScript', 'Oracle', 'AKS'])
assert evaluate_candidate(candidate) == 13

candidate = Candidate(7, ['C#', 'MongoDB', 'AWS'])
assert evaluate_candidate(candidate) == 12

candidate = Candidate(9, ['Python', 'AWS', 'GCP'])
assert evaluate_candidate(candidate) == 15

candidate = Candidate(3, ['Java', 'NoSQL', 'AKS'])
assert evaluate_candidate(candidate) == 8

candidate = Candidate