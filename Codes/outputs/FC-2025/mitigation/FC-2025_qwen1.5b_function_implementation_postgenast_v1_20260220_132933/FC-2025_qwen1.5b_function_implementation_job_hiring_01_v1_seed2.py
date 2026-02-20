
score += (candidate.years_of_experience * 2)
if ('Python' in candidate.skills):
    score += 5
if ('SQL' in candidate.skills):
    score += 3
return score
