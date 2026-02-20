if candidate.years_of_experience >= 5:
        score += 2
    if 'Python' in candidate.skills and 'JavaScript' in candidate.skills:
        score += 1
    return score

# Example usage
candidate = {
    "years_of_experience": 7,
    "skills": ["Java", "C++"]
}
print(evaluate_candidate(candidate))  # Output will depend on the actual values of years_of_experience and skills. It should be between 0 and 3.