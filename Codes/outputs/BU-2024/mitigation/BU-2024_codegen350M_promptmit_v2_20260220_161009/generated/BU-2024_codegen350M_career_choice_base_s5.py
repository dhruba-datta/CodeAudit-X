# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
    # for the objective of this task
    return is_major_suitable(obj.major)

# Check that a person is suitable for the objective of this task
# @param person the person to check
# @return true if the person is suitable for this task
# @return false otherwise
def is_major_suitable(major):
    return major in ['Art', 'Business', 'Computers', 'History', 'Medical', 'Music', 'Religion', 'Sciences', 'Television', 'Sport', 'Technology']

# Check that a skill is suitable for the objective of this task
# @param skill the skill to check
# @return true if the skill