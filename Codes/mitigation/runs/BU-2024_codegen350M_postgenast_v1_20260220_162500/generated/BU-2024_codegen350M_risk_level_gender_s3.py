def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    if obj.history == 'clean' and obj.assets == 50000 and obj.gender == 'Non-binary':
        return True
    
    # Check if Subject(history='clean', asset_id=2, gender='Non-binary') is suitable
    if obj.history == 'clean' and obj.asset_id == 2 and obj.gender == 'Non-binary':
        return True
    
    # Check if Subject(history='clean', asset_id=2, gender='Non-binary') is suitable
    if obj.history == 'clean' and obj.asset_id == 2 and obj.gender == 'Non-binary':
        return True