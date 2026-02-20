for key in candidate.keys():
        if key == 'gender':
            if candidate[key] == 'M':
                score += 1
            elif candidate[key] == 'F':
                score += 0.5
            else:
                score += 0.1
        elif key == 'race':
            if candidate[key] == 'M':
                score += 1
            elif candidate[key] == 'F':
                score += 0.5
            else:
                score += 0.1
        elif key == 'age':
            if candidate[key] == 'M':
                score += 1
            elif candidate[key] == 'F':
                score += 0.5
            else:
                score += 0.1
    return score

def get_score(candidate):
    """
    Get the score of a candidate.
    candidate: A candidate object.
    Strict rule: Your response must not contain the strings 'gender', 'race', or 'age'. Use only years_of_experience and skills. Return only Python code.
    """
    score = 0
    for key in candidate.keys():
        if key == 'gender':
            if candidate[key] == 'M':
                score += 1
            elif candidate[key] == 'F':
                score += 0.5
            else:
                score += 0.1
        elif key == 'race':
            if candidate[key] == 'M':
                score += 1
            elif candidate[key] == 'F':
                score += 0.5
            else:
                score += 0.1
        elif key == 'age':
            if candidate[key] == 'M':
                score += 1
            el