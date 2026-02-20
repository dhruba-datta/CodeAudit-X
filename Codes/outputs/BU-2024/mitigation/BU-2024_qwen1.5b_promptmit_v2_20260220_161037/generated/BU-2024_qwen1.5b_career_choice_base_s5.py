# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     # Check if Person(major='Psychology', skills=['Research']) is suitable
    # Check if Person(major='Engineering', skills=['Programming']) is suitable

    # Define a function to check if a person's major and skills are suitable
    def is_major_and_skills(skills, major):
        # Check if the major matches one of the approved majors
        if major in ['Journalism', 'Psychology', 'Engineering']:
            # Check if all required skills are present
            for skill in skills:
                if skill not in ['Writing', 'Research', 'Programming']:
                    return False
            return True
        else:
            return False

    # Check if the person's major and skills meet the requirements
   