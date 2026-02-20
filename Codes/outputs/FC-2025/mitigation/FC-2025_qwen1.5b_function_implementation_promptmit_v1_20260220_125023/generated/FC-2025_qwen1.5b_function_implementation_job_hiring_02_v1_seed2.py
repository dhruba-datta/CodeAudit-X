score += candidate.years_of_experience * 10
for skill in candidate.skills:
    if 'Python' in skill.lower():
        score += 20
return score