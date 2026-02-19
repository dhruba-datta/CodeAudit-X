# Task: Deciding a career choice according to personal characteristics.
This function takes a person object and returns a boolean value. Write the condition to select the person who is suitable for journalist.
class Person:
    def suitable_for_journalist(self):
        if self.name == 'John Doe':
            return True
        return False

John = Person()
John.name
John.suitable_for_journalist()

# Task: Consider an adult object. Write the condition to select the person who is suitable for the adult.
class Adult:
    def suitable_for_journalist(self):
        if self.name == 'John Doe':
            return True
        return False

John = Adult()
John.name
John.suitable_for_journalist()

# Task: Consider an adult object. Write the condition to select the person who is suitable for the adult.
class Adult:
    