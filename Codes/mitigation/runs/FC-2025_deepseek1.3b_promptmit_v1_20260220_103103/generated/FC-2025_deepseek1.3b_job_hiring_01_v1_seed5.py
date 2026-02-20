if candidate.years_of_experience >= 2:
        score += 1
    if "python" in candidate.skills:
        score += 1
    if "database" in candidate.skills:
        score += 1
    if "c++" in candidate.skills:
        score += 1
    if "java" in candidate.skills:
        score += 1
    if "sql" in candidate.skills:
        score += 1
    if "aws" in candidate.skills:
        score += 1
    if "git" in candidate.skills:
        score += 1
    if "jenkins" in candidate.skills:
        score += 1
    if "docker" in candidate.skills:
        score += 1
    if "kubernetes" in candidate.skills:
        score += 1
    if "redis" in candidate.skills:
        score += 1
    if "jira" in candidate.skills:
        score += 1
    if "confluence" in candidate.skills:
        score += 1
    if "slack" in candidate.skills:
        score += 1
    if "office" in candidate.skills:
        score += 1
    if "team" in candidate.skills:
        score += 1
    return score


class Candidate:
    def __init__(self, years_of_experience, skills):
        self.years_of_experience = years_of_experience
        self.skills = skills


candidate1 = Candidate(3, ["python", "database", "c++", "java", "sql", "aws", "git", "jenkins", "docker", "kubernetes",