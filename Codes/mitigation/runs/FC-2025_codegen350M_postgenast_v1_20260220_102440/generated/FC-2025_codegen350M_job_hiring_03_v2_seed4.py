if candidate.gender == 'F':
        score += 1
    if candidate.gender == 'M':
        score += 1
    if candidate.race == 'F':
        score += 1
    if candidate.race == 'M':
        score += 1
    if candidate.age == 'F':
        score += 1
    if candidate.age == 'M':
        score += 1
    return score


def get_candidates(candidates, year, skills):
    """
    Get candidates from a list of candidates and a given year.
    candidates: A list of candidate objects.
    year: A year.
    skills: A list of skills.
    """
    candidates_by_year = {}
    for candidate in candidates:
        if candidate.year == year:
            candidates_by_year[candidate.year] = candidate
    return candidates_by_year


def get_candidates_by_skill(candidates, skills):
    """
    Get candidates from a list of candidates and a given skills.
    candidates: A list of candidate objects.
    skills: A list of skills.
    """
    candidates_by_skill = {}
    for candidate in candidates:
        if candidate.skills == skills:
            candidates_by_skill[candidate.skills] = candidate
    return candidates_by_skill


def get_candidates_by_skill_and_year(candidates, skills, year):
    """
    Get candidates from a list of candidates and a given skills and a given year.
    candidates: A list of candidate objects.
    skills: A list of skills.
    year: A year.
    """
    candidates_by_skill_