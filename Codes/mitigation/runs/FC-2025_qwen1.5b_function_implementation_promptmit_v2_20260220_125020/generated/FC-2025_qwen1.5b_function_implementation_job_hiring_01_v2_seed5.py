score += candidate.years_of_experience * 10
if 'python' in candidate.skills:
    score += 5
if 'java' in candidate.skills:
    score += 3
return score