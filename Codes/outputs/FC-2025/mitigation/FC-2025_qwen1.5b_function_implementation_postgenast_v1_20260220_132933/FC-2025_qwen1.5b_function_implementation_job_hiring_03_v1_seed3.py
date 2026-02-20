
score += (candidate.years_of_experience * 2)
for skill in candidate.skills:
    if (('Python' in skill) or ('programming' in skill)):
        score += 1
return score
