# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if (obj['major'] in ['Journalism', 'Writing', 'Social Science', 'Business', 'Science']) and \
            ('skills' not in obj and 'income' not in obj and 'history' not in obj):
        return False
    # Check if Person(major='Economics', skills=['Writing'], gender='Female') is suitable
    if (obj['major'] in ['Economics', 'Writing', 'Social Science', 'Business', 'Science']) and \
            ('skills' not in obj and 'income' not in obj and 'history' not in obj):
        return False
    # Check if Person(major='Business', skills=['