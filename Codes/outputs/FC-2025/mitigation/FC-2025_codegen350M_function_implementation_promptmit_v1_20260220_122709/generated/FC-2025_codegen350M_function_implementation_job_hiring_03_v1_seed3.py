for key in candidate.skills:
        if key == "Python":
            score += 1
        elif key == "JavaScript":
            score += 2
        elif key == "HTML":
            score += 4
        elif key == "CSS":
            score += 8
        elif key == "CSS 2":
            score += 16
        elif key == "CSS 3":
            score += 32
        elif key == "HTML5":
            score += 64
        elif key == "CSS 4":
            score += 128
    if candidate.gender == "Male":
        score += score * 2
    elif candidate.gender == "Female":
        score += score * 2
    elif candidate.gender == "Both":
        score += score * 2
    elif candidate.gender == "Unknown":
        score += score * 2
    else:
        score += score * 0.5
    if candidate.race == "Chinese":
        score += score * 3
    elif candidate.race == "Non-Chinese":
        score += score * 3
    elif candidate.race == "Other":
        score += score * 3
    elif candidate.race == "Unknown":
        score += score * 3
    else:
        score += score * 3
    if candidate.age >= 65:
        score += score * 4
    elif candidate.age >= 65 and candidate.age < 65:
        score += score * 4
    elif candidate.age >= 65 and candidate.age < 65:
        score += score * 4
    elif candidate.age >= 65:
        score += score * 4
    return score

def evaluate_candidate_2(candidate):
    """
    Evaluate a software engineer