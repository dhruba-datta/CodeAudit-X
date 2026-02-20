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
    if 'Go' in candidate.skills:
        score += 1
    if 'PHP' in candidate.skills:
        score += 1
    if 'MATLAB' in candidate.skills:
        score += 1
    if 'R' in candidate.skills:
        score += 1
    return score


def evaluate_candidates(candidates):
    """
    Evaluate a list of software engineer candidates.
    candidates: A list of candidate objects.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    scores = [evaluate_candidate(candidate) for candidate in candidates]
    return scores


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills

# Test the function
candidates = [Candidate(6, ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Swift', 'Go', 'PHP', 'MATLAB', 'R']