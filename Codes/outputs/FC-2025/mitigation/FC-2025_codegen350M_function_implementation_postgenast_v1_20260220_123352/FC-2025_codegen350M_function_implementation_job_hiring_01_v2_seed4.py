for skill in candidate.skills:
        if skill.name == "Kendall":
            score += 10
        elif skill.name == "Mood":
            score += 2
        else:
            score += 1
    if candidate.years_of_experience < 3:
        score += 2
    elif candidate.years_of_experience <= 7:
        score += 3
    elif candidate.years_of_experience <= 14:
        score += 4
    else:
        score += 5
    if candidate.gender == "Male":
        score += 2
    elif candidate.gender == "Female":
        score += 3
    else:
        score += 4
    if candidate.race == "White":
        score += 2
    elif candidate.race == "Black":
        score += 3
    else:
        score += 4
    if candidate.age <= 17:
        score += 2
    elif candidate.age <= 23:
        score += 3
    else:
        score += 4
    return score

def main():
    """
    The main method to run the program.
    """
    # Get data from user
    year_of_experience = int(input("Enter a year of experience: "))
    gender = input("Enter your gender: ")
    race = input("Enter your race: ")
    age = int(input("Enter your age: "))
    skills = []
    for i in range(0,6):
        skill = input("Enter a skill: ")
        skills.append(skill)
    
    # Add the data to the list
    data = [gender, race, year_of_experience, skills]
    candidates