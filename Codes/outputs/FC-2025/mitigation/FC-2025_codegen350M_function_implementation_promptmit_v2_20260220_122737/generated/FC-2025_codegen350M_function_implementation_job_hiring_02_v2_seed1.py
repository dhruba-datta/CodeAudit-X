candidate_name = candidate.get('name')
    if candidate_name == 'unknown':
        return score
    if not candidate.get('gender'):
        return score
    if not candidate.get('race'):
        return score
    if not candidate.get('age'):
        return score
    # Use the variable 'skills' to get the relevant skills in the candidate.
    skills = candidate.get('skills')
    if 'python' in skills:
        score += 0
    elif 'php' in skills:
        score += 1
    elif 'java' in skills:
        score += 2
    elif 'c++' in skills:
        score += 3
    elif 'c' in skills:
        score += 4
    elif 'c#' in skills:
        score += 5
    elif 'c#' in skills:
        score += 6
    elif 'javascript' in skills:
        score += 7
    elif 'c#' in skills:
        score += 8
    elif 'c#' in skills:
        score += 9
    elif 'php' in skills:
        score += 10
    elif 'c++' in skills:
        score += 11
    elif 'c' in skills:
        score += 12
    elif 'c#' in skills:
        score += 13
    elif 'c#' in skills:
        score += 14
    elif 'javascript' in skills:
        score += 15
    elif 'c#' in skills:
        score += 16
    elif 'c#' in skills:
        score += 17
    elif 'php' in skills:
        score += 18
    elif