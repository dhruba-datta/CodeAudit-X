if candidate.years_of_experience >= 5:
    score += 2

for skill in candidate.skills:
    if skill == "Python":
        score += 3
    elif skill == "Java":
        score += 1
    else:
        score -= 1

return score