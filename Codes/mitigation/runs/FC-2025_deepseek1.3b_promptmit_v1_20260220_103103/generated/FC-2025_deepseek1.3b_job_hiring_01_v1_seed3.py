if candidate.years_of_experience > 5:
        score += 1

    if "Python" in candidate.skills:
        score += 1

    if "Data Science" in candidate.skills:
        score += 1

    if "Machine Learning" in candidate.skills:
        score += 1

    if "Android" in candidate.skills:
        score += 1

    if "iOS" in candidate.skills:
        score += 1

    if "Web Development" in candidate.skills:
        score += 1

    if "Javascript" in candidate.skills:
        score += 1

    if "DevOps" in candidate.skills:
        score += 1

    if "AWS" in candidate.skills:
        score += 1

    if "Docker" in candidate.skills:
        score += 1

    if "Kubernetes" in candidate.skills:
        score += 1

    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(6, ["Python", "Data Science", "Machine Learning", "Android", "iOS", "Web Development", "Javascript", "DevOps", "AWS", "Docker", "Kubernetes"])
candidate2 = Candidate(3, ["Python", "Data Science", "Machine Learning", "Android", "iOS", "Web Development", "Javascript", "DevOps", "AWS", "Docker", "Kubernetes"])
candidate