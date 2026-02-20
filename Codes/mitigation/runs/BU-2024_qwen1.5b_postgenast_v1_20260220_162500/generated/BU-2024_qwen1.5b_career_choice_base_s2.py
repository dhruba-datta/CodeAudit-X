def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     return obj.major == 'Journalism' and all(skill in obj.skills for skill in ['Writing'])
