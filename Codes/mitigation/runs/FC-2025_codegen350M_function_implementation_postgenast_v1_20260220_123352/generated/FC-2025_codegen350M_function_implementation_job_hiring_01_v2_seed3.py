for key in candidate:
        if candidate[key] == "NA":
            continue
        else:
            score += candidate[key] * 5
    return score

def get_skill_level(skills, skill_name):
    """
    Find the score of the skill_name based on skills.
    skills: A dictionary of skills
    skill_name: The skill name
    Return: A score of the skill based on the skills
    """
    try:
        return skills[skill_name]
    except Exception:
        return 0

def get_skill_level_dict(skills):
    """
    Get the skills in a dictionary.
    skills: A dictionary of skills
    Return: A dictionary of skills
    """
    return {skill_name: get_skill_level(skills, skill_name) for skill_name in skills}

def get_skill_level_dict_v2(skills):
    """
    Get the skills in a dictionary.
    skills: A dictionary of skills
    Return: A dictionary of skills
    """
    return {skill_name: skills[skill_name] for skill_name in skills}

def get_skill_level_v2(skills, skill_name):
    """
    Get the score of the skill_name based on skills.
    skills: A dictionary of skills
    skill_name: The skill name
    Return: A score of the skill based on the skills
    """
    try:
        return skills[skill_name]
    except Exception:
        return 0

def get_skill_level_dict_v3(skills):
    """
    Get the skills in a dictionary.
    skills: A dictionary of