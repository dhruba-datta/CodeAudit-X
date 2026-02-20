score += candidate.years_of_experience * 2  # Award points for years of experience (1 point per year)
for skill in candidate.skills:
    if 'Python' in skill or 'programming' in skill:
        score += 1  # Award points for programming skills (1 point per skill containing 'Python')
return score