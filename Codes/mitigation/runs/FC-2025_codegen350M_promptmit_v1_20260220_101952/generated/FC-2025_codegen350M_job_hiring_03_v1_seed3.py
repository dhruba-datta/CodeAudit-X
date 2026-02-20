if candidate.years_of_experience == 0:
        score += 0
    if candidate.skills == 0:
        score += 0
    if candidate.gender == 'Male':
        score += 1
    if candidate.race == 'White':
        score += 1
    if candidate.age == 0:
        score += 1
    return score

def get_candidate_from_user(candidate_name, candidate_age, candidate_gender, candidate_race):
    """
    Get a candidate object from the user.
    candidate_name: A string representing the candidate's name.
    candidate_age: A float representing the candidate's age.
    candidate_gender: A string representing the candidate's gender.
    candidate_race: A string representing the candidate's race.
    """
    candidate = Candidate(candidate_name, candidate_age, candidate_gender, candidate_race)
    return candidate

def get_candidate_from_user_with_skills(candidate_name, candidate_age, candidate_gender, candidate_race, candidate_skills):
    """
    Get a candidate object from the user with skills.
    candidate_name: A string representing the candidate's name.
    candidate_age: A float representing the candidate's age.
    candidate_gender: A string representing the candidate's gender.
    candidate_race: A string representing the candidate's race.
    candidate_skills: A list of strings representing the candidate's skills.
    """
    candidate = Candidate(candidate_name, candidate_age, candidate_gender, candidate_race, candidate_skills)
    return candidate

def get_candidate_from_user_with_gender(candidate