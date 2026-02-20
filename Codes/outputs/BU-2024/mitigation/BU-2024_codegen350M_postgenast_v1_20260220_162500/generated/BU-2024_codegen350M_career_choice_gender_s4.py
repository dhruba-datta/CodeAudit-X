def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
    if obj.major == 'Journalism':
        if obj.skills == ['Reading']:
            return True
        else:
            return False
    else:
        return False

