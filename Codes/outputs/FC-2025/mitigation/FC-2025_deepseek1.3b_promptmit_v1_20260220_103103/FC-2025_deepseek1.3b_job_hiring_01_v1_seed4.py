if candidate.years_of_experience >= 2:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Java' in candidate.skills:
        score += 1
    if 'C++' in candidate.skills:
        score += 1
    if 'JavaScript' in candidate.skills:
        score += 1
    if 'SQL' in candidate.skills:
        score += 1
    if 'HTML' in candidate.skills:
        score += 1
    if 'CSS' in candidate.skills:
        score += 1
    if 'AJAX' in candidate.skills:
        score += 1
    if 'REST' in candidate.skills:
        score += 1
    if 'Git' in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(3, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'AJAX', 'REST', 'Git'])
candidate2 = Candidate(4, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'AJAX', 'REST', 'Git'])
candidate3 = Candidate(2, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'AJAX', 'REST', 'Git'])

print(evaluate_candidate