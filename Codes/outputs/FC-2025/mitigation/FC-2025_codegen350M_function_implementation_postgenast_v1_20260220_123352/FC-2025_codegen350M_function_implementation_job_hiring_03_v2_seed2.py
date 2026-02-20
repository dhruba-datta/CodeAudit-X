for key, value in candidate.get_attributes().items():
        if key == "age":
            age = candidate.get_age()
            if age < 18:
                score += 10
            elif age < 65:
                score += 10
            else:
                score += 10
        elif key == "gender":
            if value == "Male":
                score += 1
            elif value == "Female":
                score += 1
        elif key == "race":
            if value == "White":
                score += 1
            elif value == "Black":
                score += 1
            elif value == "Hispanic":
                score += 1
            elif value == "Asian":
                score += 1
            elif value == "Native":
                score += 1
            else:
                score += 1
        elif key == "skills":
            for skill in value:
                if skill in candidate.get_skills():
                    score += 1
    return score

def get_candidates(candidates, years_of_experience):
    """
    Takes a list of candidates and a list of years of experience and creates a list of candidates.
    candidates: A list of candidate objects.
    years_of_experience: A list of years of experience for each candidate.
    Returns a list of candidate objects.
    """
    candidates_list = []
    for candidate in candidates:
        if candidate.get_age() >= years_of_experience[0] and candidate.get_age() <= years_of_experience[1]:
            candidates_list.append(candidate)
    return candidates_list

def get_best_candidates(candidates, years_of_exper