score += candidate.years_of_experience * 2  # Award points for years of experience
if 'Python' in candidate.skills:
    score += 5  # Award points for proficiency in Python
if 'SQL' in candidate.skills:
    score += 3  # Award points for proficiency in SQL
if 'C++' in candidate.skills:
    score += 1  # Award points for proficiency in C++
return score