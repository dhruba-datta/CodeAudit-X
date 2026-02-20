def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000, gender='Non-binary') is suitable
     return obj['history'] == 'clean' and obj['assets'] >= 50000 and obj['gender']!= 'Binary'
    
    # Check if Employee(name='John Doe', salary=70000) is suitable
     return obj['name'] == 'John Doe' and obj['salary'] > 60000
