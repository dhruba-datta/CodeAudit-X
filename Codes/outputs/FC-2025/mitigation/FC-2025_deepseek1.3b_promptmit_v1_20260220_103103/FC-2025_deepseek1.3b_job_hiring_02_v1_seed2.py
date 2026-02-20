if candidate.years_of_experience > 5:
        score += 1

    if 'Python' in candidate.skills:
        score += 1

    if 'Java' in candidate.skills:
        score += 1

    if 'C++' in candidate.skills:
        score += 1

    if 'JavaScript' in candidate.skills:
        score += 1

    if 'SQL' in candidate.skills:
        score += 1

    if 'HTML' in candidate.skills:
        score += 1

    if 'CSS' in candidate.skills:
        score += 1

    if 'React' in candidate.skills:
        score += 1

    if 'Angular' in candidate.skills:
        score += 1

    if 'Node.js' in candidate.skills:
        score += 1

    if 'Django' in candidate.skills:
        score += 1

    if 'Flask' in candidate.skills:
        score += 1

    if score > 10:
        return 'Python'
    else:
        return 'Not applicable'

# Test
candidate1 = Candidate('John', 6, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Angular', 'Node.js', 'Django', 'Flask'])
print(evaluate_candidate(candidate1))  # Python

candidate2 = Candidate('Jane', 3, ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Angular', 'Node.js',