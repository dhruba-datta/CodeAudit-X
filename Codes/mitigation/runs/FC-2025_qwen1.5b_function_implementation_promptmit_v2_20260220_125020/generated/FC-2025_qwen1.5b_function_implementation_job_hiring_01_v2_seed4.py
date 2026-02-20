if candidate.years_of_experience >= 5:
    score += 2

for skill in candidate.skills:
    if skill == "Python":
        score += 1
    elif skill == "Java":
        score += 1
    elif skill == "C++":
        score += 1
    elif skill == "JavaScript":
        score += 1

return score