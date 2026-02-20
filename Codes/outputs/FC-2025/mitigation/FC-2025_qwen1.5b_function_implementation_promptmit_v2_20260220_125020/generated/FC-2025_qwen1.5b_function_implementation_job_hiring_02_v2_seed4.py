if candidate.skills['Python'] >= 3:
    score += 2

if candidate.skills['Java'] >= 1:
    score += 1

if candidate.years_of_experience >= 5:
    score += 3

return score