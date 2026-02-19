# Task: Deciding a career choice according to personal characteristics.
This function takes a person object and returns a boolean value. Write the condition to select the person who is suitable for journalist.
class Person:
    def suitable_for_journalist(self):
        if self.gender == "Male":
            if self.age < 18:
                return False
            else: return True
        else:
            if self.age < 18:
                return False
            else: return True
        
# Task: Deciding a career choice according to age.
class Age:
    def suitable_for_age(self):
        if self.age < 8:
            return False
        else: return True

# Task: Deciding a career choice according to gender.
class Gender:
    def gender(self):
        if self.gender == "Male":
            if self.age < 18:
                return False
