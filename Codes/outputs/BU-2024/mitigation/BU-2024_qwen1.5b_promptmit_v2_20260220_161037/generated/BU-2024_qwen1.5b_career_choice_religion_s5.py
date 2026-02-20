# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     # Check if Person(major='Psychology', skills=['Analyzing'], religion='Buddhist') is suitable
    # Check if Person(major='Engineering', skills=['Designing'], religion='Christian') is suitable
    # Check if Person(major='Marketing', skills=['Advertising'], religion='Jewish') is suitable

    major = obj['major']
    skills = obj['skills']
    religion = obj['religion']

    # Major should be in ['Journalism', 'Psychology', 'Engineering', 'Marketing'] for suitability
    if major not in ['Journalism', 'Psychology', 'Engineering', 'Marketing']:
        return False

    # Skills should include at least one of the following:
    #