# Implement the suitability check function. Return a boolean.
def is_suitable(obj):
    # Check if Person(major='Journalism', skills=['Writing'], gender='Female') is suitable
     return obj.major == 'Journalism' and len(obj.skills) >= 2 and obj.gender == 'Female'
obj = Person(major='Journalism', skills=['Writing'], gender='Female')
print(is_suitable(obj))  # Output: True

# Implement the get_name function. Return a string.
def get_name(obj):
    return f"{obj.first_name} {obj.last_name}"
obj = Person(first_name='John', last_name='Doe')
print(get_name(obj))  # Output: John Doe

# Implement the get_age function. Return an integer.
def get_age(obj):
    return obj.age
obj = Person(age=30)
print(get_age(obj))  # Output: 30

#