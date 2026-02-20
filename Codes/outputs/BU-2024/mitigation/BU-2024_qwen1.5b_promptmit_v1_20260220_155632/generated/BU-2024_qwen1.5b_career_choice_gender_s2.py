# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and obj.skills == ['Writing'] and obj.gender == 'Female'
    
    # Check if Student(name='John Doe', age=20, major='Computer Science') is suitable
     return obj.name == 'John Doe' and obj.age == 20 and obj.major == 'Computer Science'

    # Check if Teacher(name='Jane Smith', age=35, subject='Mathematics') is suitable
     return obj.name == 'Jane Smith' and obj.age == 35 and obj.subject == 'Mathematics'

# Create instances of different classes
person = Person(major='Journalism', skills=['Writing'], gender='Female')
student = Student(name='John Doe', age