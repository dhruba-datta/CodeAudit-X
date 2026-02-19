Return only users where 'active' is True. Implement filter_users(users). Each user has name, active.
    """
    return [user for user in users if user.active]

def get_users_by_email(email):
    """
    Returns users where email address matches the given email.
    """
    return [user for user in users if user.email == email]

def get_users_by_username(username):
    """
    Returns users where username starts with the given username.
    """
    return [user for user in users if user.username.startswith(username)]

def get_