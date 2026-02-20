for key, value in candidate.get_attributes().items():
        if key == "years_of_experience":
            score += value
        elif key == "skills":
            score += value
        elif key == "gender":
            if value == "male":
                score += 1
            elif value == "female":
                score += 1
            elif value == "unknown":
                score += 0
            else:
                score += -1
        else:
            if value == "unknown":
                score += -1
            elif value == "male":
                score += 2
            elif value == "female":
                score += 2
            elif value == "yes":
                score += 3
            elif value == "no":
                score += 3
            elif value == "no":
                score += 3
            else:
                score += 0
    return score

def get_candidates(candidates, candidates_file):
    """
    Read all the candidates in the file and assign them the appropriate candidate.
    candidates: A list of candidates.
    candidates_file: A file with all the candidates.
    """
    with open(candidates_file, "r") as file:
        for line in file:
            candidate = Candidate()
            candidate.set_names(line.split(",")[0].strip())
            candidate.set_email(line.split(",")[1].strip())
            candidate.set_skills(line.split(",")[2].strip())
            candidates.append(candidate)

def write_candidates(candidates, candidates_file):
    """
    Write the candidate objects to a file.
    candidates