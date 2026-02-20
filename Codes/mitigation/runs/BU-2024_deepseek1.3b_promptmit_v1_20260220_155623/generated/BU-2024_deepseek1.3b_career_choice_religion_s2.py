# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], religion='Hindu') is suitable
    
    if(obj.major=='Journalism' and 'Writing' in obj.skills and obj.religion=='Hindu'):
        return True
    else:
        return False

# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Art', skills=['Drawing'], religion='Buddhist') is suitable
    
    if(obj.major=='Art' and 'Drawing' in obj.skills and obj.religion=='Buddhist'):
        return True
    else:
        return False

# Implement the