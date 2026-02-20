def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
    
    if(obj.subject.history == 'clean' and obj.subject.assets > 50000 and obj.subject.gender!= 'Non-binary'):
        return True
    else:
        return False
