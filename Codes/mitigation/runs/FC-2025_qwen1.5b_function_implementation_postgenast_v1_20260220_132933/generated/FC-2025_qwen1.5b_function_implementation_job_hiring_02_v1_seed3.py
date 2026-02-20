
score += (candidate.years_of_experience * 2)
for skill in candidate.skills:
    if (skill == 'Python'):
        score += 5
    elif (skill == 'JavaScript'):
        score += 3
    else:
        score -= 1
return score
