
score += (candidate.years_of_experience * 2)
if ('Python' in candidate.skills):
    score += 1
if ('Machine Learning' in candidate.skills):
    score += 1
return score
