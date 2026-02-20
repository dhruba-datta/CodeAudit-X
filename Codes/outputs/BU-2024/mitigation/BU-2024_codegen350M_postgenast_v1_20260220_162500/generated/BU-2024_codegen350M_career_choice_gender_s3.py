def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.gender == 'Female':
        return True
