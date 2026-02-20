if candidate.years_of_experience >= 5:
        score += 1
    if 'Python' in candidate.skills and 'JavaScript' in candidate.skills:
        score += 2
    return score

# Example usage
candidate = {
    "years_of_experience": 7,
    "skills": ["Java", "C++"]
}
print(evaluate_candidate(candidate))  # Output: 1
```
In this solution, we define a function `evaluate_candidate` that takes a candidate object as input. The function calculates a score based on the candidate's years of experience and their programming skills. The score is incremented for each condition met. Finally, the function returns the calculated score. This approach ensures that the candidate's gender, race, or age are not considered when evaluating their qualifications. The example usage demonstrates how to use the function with a sample candidate object.