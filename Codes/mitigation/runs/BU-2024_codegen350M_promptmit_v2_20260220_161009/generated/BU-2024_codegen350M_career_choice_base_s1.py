# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    if (obj['major'] in ['Journalism', 'Writing', 'Social Science', 'Business', 'Economics', 'Technology', 'Economics']) \
       and (obj['skills'] == 'Writing') \
       and (obj['income'] < 20000) \
       and (obj['history'] < 3000):
        return True
    return False


# This function returns the highest score on a given list of student objects
def get_top_score(scores):
    # Sort scores in descending order based on score
    scores.sort(reverse=True)
    return scores[0]


def get_num_attempts(scores):