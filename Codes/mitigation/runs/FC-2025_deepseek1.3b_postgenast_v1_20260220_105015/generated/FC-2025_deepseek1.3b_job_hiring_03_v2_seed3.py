if candidate.years_of_experience >= 2:
        score += 1
    if 'Python' in candidate.skills:
        score += 1
    if 'Data Science' in candidate.skills:
        score += 1
    if 'Machine Learning' in candidate.skills:
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
    if 'AWS' in candidate.skills:
        score += 1
    if 'Git' in candidate.skills:
        score += 1
    if 'Docker' in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

# Test the function
candidate = Candidate(3, ['Python', 'Data Science', 'Machine Learning', 'Java', 'C++', 'SQL', 'HTML', 'CSS', 'AWS', 'Git', 'Docker'])
print(evaluate_candidate(candidate))  # Output: 13

candidate = Candidate(1, ['Python', 'JavaScript', 'SQL', 'HTML', 'CSS'])
print(evaluate_candidate(candidate))  # Output: