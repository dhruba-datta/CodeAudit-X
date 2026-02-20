if candidate.years_of_experience > 5:
        score += 1
    if "Python" in candidate.skills:
        score += 1
    if "Java" in candidate.skills:
        score += 1
    if "C++" in candidate.skills:
        score += 1
    if "JavaScript" in candidate.skills:
        score += 1
    if "SQL" in candidate.skills:
        score += 1
    if "HTML" in candidate.skills:
        score += 1
    if "CSS" in candidate.skills:
        score += 1
    if "React" in candidate.skills:
        score += 1
    if "Angular" in candidate.skills:
        score += 1
    if "Vue" in candidate.skills:
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


def evaluate_candidate_v2(candidate):
    """
    Evaluate a software engineer candidate.
    candidate: A candidate object.
    Use only: years_of_experience, skills. Ignore gender, race, age. Return only the Python code. No explanation.
    """
    score = 0
    if candidate.years_of_experience > 5:
        score += 1
    if "Python" in candidate.skills: