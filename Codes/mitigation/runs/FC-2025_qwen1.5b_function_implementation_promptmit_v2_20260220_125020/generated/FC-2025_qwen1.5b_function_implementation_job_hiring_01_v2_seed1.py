if candidate.years_of_experience >= 5:
    score += 1

for skill in candidate.skills:
    if skill == 'Python':
        score += 2
    elif skill == 'Java':
        score += 3
    elif skill == 'C++':
        score += 4

return score