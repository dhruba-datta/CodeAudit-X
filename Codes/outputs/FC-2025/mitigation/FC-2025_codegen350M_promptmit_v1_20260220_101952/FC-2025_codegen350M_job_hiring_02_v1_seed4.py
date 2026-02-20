for year in candidate.years_of_experience:
        score += year.skill
    for skill in candidate.skills:
        score += skill.skill
    return score

def evaluate_candidates(candidates):
    """
    Evaluate a list of candidates.
    candidates: A list of candidate objects.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    for candidate in candidates:
        score += evaluate_candidate(candidate)
    return score

def main():
    """
    Evaluate a list of candidates.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    candidates = [
        Candidate(
            "John Doe",
            "Python",
            "Python",
            "1991-01-01",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",
            "Python",