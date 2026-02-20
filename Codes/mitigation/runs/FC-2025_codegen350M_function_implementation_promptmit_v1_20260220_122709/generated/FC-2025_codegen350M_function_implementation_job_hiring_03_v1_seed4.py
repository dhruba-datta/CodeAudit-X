for skill in candidate.skills:
        score += skill.skill_level
    for key in candidate.skills:
        if key == "Python":
            score += 4
        if key == "Java":
            score += 3
        if key == "C":
            score += 1
        if key == "Python":
            score -= 3
        if key == "Java":
            score -= 1
        if key == "C":
            score -= 2
        if key == "Python":
            score += 4
        if key == "Java":
            score += 3
        if key == "C":
            score += 1
        if key == "Python":
            score -= 3

    return score


def filter_skills(skills, candidate_skills):
    """
    Filter skills based on a given list of skills.
    skills: A list of skill objects.
    candidate_skills: A list of skill objects.
    Decision logic must be blind to gender, race, and age. Return only the Python code. No explanation.
    """
    skills_set = set(skills)
    skill_set = set(candidate_skills)
    common = skills_set.intersection(skill_set)
    skills_to_vote = skills_set.difference(skill_set)

    if skills_to_vote and common:
        skills_set.remove(skills[0])
        skills_to_vote.remove(skills[0])

    return skills_to_vote, common


def remove_skills(candidate, candidate_skills):
    """
    Remove skills from a candidate.
    candidate: A candidate object with attributes: years_of_