score += candidate.years_of_experience * 10
if 'Python' in candidate.skills:
    score += 5
if 'JavaScript' in candidate.skills:
    score += 3
return score