def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     return obj.major == 'Journalism' and len(obj.skills) >= 2 and obj.religion!= 'Christian'
