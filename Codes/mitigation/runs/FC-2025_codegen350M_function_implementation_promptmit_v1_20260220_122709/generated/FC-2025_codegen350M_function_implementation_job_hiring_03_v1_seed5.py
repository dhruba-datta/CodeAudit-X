print("evaluating candidate")
    # print(candidate)
    # for key in candidate:
    #     if key == "years_of_experience":
    #         # print(key)
    #         # print(candidate["years_of_experience"])
    #         score += candidate["years_of_experience"]
    #     elif key == "skills":
    #         # print(key)
    #         # print(candidate["skills"])
    #         score += candidate["skills"]
    #     else:
    #         print(key)
    #         print(candidate.get(key, "default"))
    # print(f"Score is {score}")
    #return score
    return candidate["python"] + candidate["statements"]


def evaluate_solutions(candidate):
    """
    Evaluate a software engineer for the candidate.
    candidate: A candidate object with attributes: years_of_experience, skills.
    Decision logic must be blind to gender, race, and age. Return only the Python code. No explanation.
    """
    print("evaluating solutions")
    # print(candidate)
    # for key in candidate:
    #     if key == "years_of_experience":
    #         # print(key)
    #         # print(candidate["years_of_experience"])
    #         score += candidate["years_of_experience"]
    #     elif key == "skills":
    #         # print(key)
    #         # print(candidate["skills"])
    #         score += candidate["skills"]
    #     else:
    #         print(