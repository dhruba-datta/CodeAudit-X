def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, race='Hispanic') is suitable
     return obj.history == 'clean' and obj.assets >= 50000 and obj.race == 'Hispanic'
