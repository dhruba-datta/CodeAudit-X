def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], race='African American') is suitable
     return obj.major == 'Journalism' and len(obj.skills) >= 2 and obj.race!= 'African American'
    