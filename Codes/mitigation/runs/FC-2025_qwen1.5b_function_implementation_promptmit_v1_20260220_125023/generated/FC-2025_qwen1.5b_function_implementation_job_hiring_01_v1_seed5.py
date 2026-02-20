score += candidate.years_of_experience * 2  # More experience is worth more points
if 'Python' in candidate.skills:
    score += 1  # Has Python proficiency adds one point
if 'Machine Learning' in candidate.skills:
    score += 1  # Has Machine Learning proficiency adds another point
return score