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
    if 'React' in candidate.skills:
        score += 1
    if 'Angular' in candidate.skills:
        score += 1
    if 'Node.js' in candidate.skills:
        score += 1
    if 'Express' in candidate.skills:
        score += 1
    if 'Django' in candidate.skills:
        score += 1
    if 'Kubernetes' in candidate.skills:
        score += 1
    return score

class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

candidate1 = Candidate(3, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Angular', 'Node.js', 'Express', 'Django', 'Kubernetes'])
candidate2 = Candidate(5, ['Python', 'Java', 'C++', 'SQL', 'HTML', 'CSS', 'React', 'Angular