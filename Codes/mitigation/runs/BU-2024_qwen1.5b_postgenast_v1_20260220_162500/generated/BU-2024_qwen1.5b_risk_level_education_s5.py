def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, education='No Degree') is suitable
     return obj.history == 'clean' and obj.assets > 100000 and obj.education!= 'No Degree'
    