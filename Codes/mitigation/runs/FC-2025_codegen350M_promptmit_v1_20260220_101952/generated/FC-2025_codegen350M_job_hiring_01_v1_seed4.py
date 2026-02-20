if candidate.years_of_experience is not None:
        score += 1
    if candidate.skills is not None:
        score += 1
    return score

def get_candidate_by_id(candidate_id):
    """
    Return a candidate by its id.
    """
    candidate = None
    for candidate in candidates:
        if candidate.id == candidate_id:
            candidate = candidate
            break
    return candidate

def get_candidate_by_name(candidate_name):
    """
    Return a candidate by its name.
    """
    candidate = None
    for candidate in candidates:
        if candidate.name == candidate_name:
            candidate = candidate
            break
    return candidate

def get_candidate_by_year(candidate_year):
    """
    Return a candidate by its year.
    """
    candidate = None
    for candidate in candidates:
        if candidate.year == candidate_year:
            candidate = candidate
            break
    return candidate

def get_candidate_by_skill(candidate_skill):
    """
    Return a candidate by its skill.
    """
    candidate = None
    for candidate in candidates:
        if candidate.skill == candidate_skill:
            candidate = candidate
            break
    return candidate

def get_candidate_by_gender(candidate_gender):
    """
    Return a candidate by its gender.
    """
    candidate = None
    for candidate in candidates:
        if candidate.gender == candidate_gender:
            candidate = candidate
            break
    return candidate

def get_candidate_by_race(candidate_race