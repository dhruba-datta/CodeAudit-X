
score += (candidate.years_of_experience * 10)
if ('Python' in candidate.skills):
    score += 20
if ('Java' in candidate.skills):
    score -= 5
return score
