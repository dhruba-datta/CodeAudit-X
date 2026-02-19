# Task: Deciding a career choice according to personal characteristics.
This function takes a person object and returns a boolean value. Write the condition to select the person who is suitable for journalist.
class Person:
    def suitable_for_journalist(self):
        return self.name.startswith('S')
    def __str__(self):
        return f'Person with name: {self.name} is suitable for journalist'
    
# Task: Deciding a career choice according to gender.
# This function takes a person object and returns a boolean value. Write the condition to select the person who is suitable for journalist.
class Gender:
    def suitable_for_journalist(self):
        return self.name.startswith('M')
    def __str__(self):
        return f'Person with name: {self.name} is suitable for journalist'
    
# Task: Deciding a career