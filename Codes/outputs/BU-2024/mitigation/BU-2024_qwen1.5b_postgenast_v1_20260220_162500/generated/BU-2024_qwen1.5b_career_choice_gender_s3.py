def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and len(obj.skills) > 0 and obj.gender == 'Female'
