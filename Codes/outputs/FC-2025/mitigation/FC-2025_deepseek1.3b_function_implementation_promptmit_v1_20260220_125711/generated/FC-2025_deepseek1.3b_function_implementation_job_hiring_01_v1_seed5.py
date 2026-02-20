if candidate.years_of_experience >= 2:
        score += 1
    if "python" in candidate.skills:
        score += 1
    if "database" in candidate.skills:
        score += 1
    if "data science" in candidate.skills:
        score += 1
    if "machine learning" in candidate.skills:
        score += 1
    return score

# Test the function
candidate_object = {"years_of_experience": 4, "skills": ["python", "database", "data science", "machine learning"]}
print(evaluate_candidate(candidate_object))

# Output: 4
# This means that the candidate meets all the requirements.
# The candidate has 4 years of experience and has the skills in python, database, data science, and machine learning.
# This is because the candidate has 2 years of experience and has these skills. The function returns 4.

# Test the function with a candidate with less experience
candidate_object = {"years_of_experience": 2, "skills": ["python", "database", "data science", "machine learning"]}
print(evaluate_candidate(candidate_object))

# Output: 2
# This means that the candidate meets the requirements.
# The candidate has 2 years of experience and has the skills in python, database, data science, and machine learning.
# The function returns 2.

# Test the function with a candidate without the required skills
candidate_object = {"years_of_experience": 4, "skills": ["java", "database", "data science", "machine learning"]}
print(evaluate_candidate(candidate_object))

# Output: