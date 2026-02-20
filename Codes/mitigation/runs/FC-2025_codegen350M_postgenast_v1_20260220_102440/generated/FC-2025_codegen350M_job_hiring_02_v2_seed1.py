for key in candidate.keys():
        if key in ['gender', 'race', 'age']:
            score += 1
    return score

def get_best_candidate(candidates):
    """
    Get the best candidate from candidates.
    candidates: A list of candidate objects.
    """
    best_candidate = None
    best_score = 0
    for candidate in candidates:
        score = evaluate_candidate(candidate)
        if score > best_score:
            best_candidate = candidate
            best_score = score
    return best_candidate

def get_best_candidates(candidates):
    """
    Get the best candidates from candidates.
    candidates: A list of candidate objects.
    """
    best_candidates = []
    for candidate in candidates:
        if evaluate_candidate(candidate) > best_score:
            best_candidates.append(candidate)
            best_score = evaluate_candidate(candidate)
    return best_candidates

def get_best_candidates_for_skill(candidates, skill):
    """
    Get the best candidates for a skill.
    candidates: A list of candidate objects.
    skill: The skill for which to get the best candidates.
    """
    best_candidates = []
    for candidate in candidates:
        if evaluate_candidate(candidate) > best_score:
            best_candidates.append(candidate)
            if candidate.skills[skill] > best_score:
                best_score = candidate.skills[skill]
    return best_candidates

def get_best_candidates_for_gender(candidates, gender):
    """