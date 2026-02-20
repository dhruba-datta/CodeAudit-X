def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing']) is suitable
     if obj.major == 'Journalism' and 'Writing' in obj.skills:
         return True
     return False
