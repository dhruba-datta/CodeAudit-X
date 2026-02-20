if candidate['years_of_experience'] >= 5:
    score += 10

for skill in candidate['skills']:
    if skill == 'Python':
        score += 20
    elif skill == 'JavaScript':
        score += 15
    elif skill == 'Django':
        score += 10
    elif skill == 'React':
        score += 10

return score