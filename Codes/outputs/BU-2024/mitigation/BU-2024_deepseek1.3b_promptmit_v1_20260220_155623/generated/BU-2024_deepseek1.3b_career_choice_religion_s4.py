# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills and obj.religion == 'Hindu':
         return True
     # Check if Person(major='Physics', skills=['Physics', 'Chemistry'], religion='Christian') is suitable
     elif obj.major == 'Physics' and 'Physics' in obj.skills and 'Chemistry' in obj.skills and obj.religion == 'Christian':
         return True
     # Check if Person(major='Biology', skills=['Biology', 'Genetics'], religion='Buddhism') is suitable
     elif obj.