score += candidate.years_of_experience * 2  # More experience is better
if 'Python' in candidate.skills:
    score += 5  # Proficiency in Python adds points
if 'SQL' in candidate.skills:
    score += 3  # Proficiency in SQL adds more points
return score