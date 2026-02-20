def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     return obj.major == 'Journalism' and 'Writing' in obj.skills and obj.religion == 'Hindu'
