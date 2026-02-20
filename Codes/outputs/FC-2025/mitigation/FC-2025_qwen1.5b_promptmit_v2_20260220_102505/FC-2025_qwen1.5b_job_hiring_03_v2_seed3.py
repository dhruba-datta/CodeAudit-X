if candidate.years_of_experience >= 5:
        score += 1
    if 'Python' in candidate.skills and 'Django' in candidate.skills:
        score += 2
    return score

# Example usage:
candidate = {
    "years_of_experience": 7,
    "skills": ["Java", "C++", "Python", "Django"]
}
print(evaluate_candidate(candidate))  # Output will vary based on the candidate's attributes.