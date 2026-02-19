Write filter_users(users) in Python. users is list[dict(name, active)]. Return only active=True.
    """
    if len(users) == 0:
        return []
    users = sorted(users, key=lambda user: user["name"], reverse=True)
    return [user for user in users if user["active"]]


def filter_users_by_email(users, email):
    """Filter list of users by email.
    Return only users with email=email.
    """
    return [user for user in users if user["email"] == email]


def filter_users_by_username(users