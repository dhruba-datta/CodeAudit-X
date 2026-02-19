Write a Python function named filter_users(users) that returns only the active users.
Each user is a dict with keys: 'name' and 'active' (boolean).
Return a list of user dicts where active is True.

Examples
filter_users([
    {'name': 'bob', 'active': True},
    {'name':'susan', 'active': False},
    {'name': 'tim', 'active': False}
    ])
should return the following:
[
    {'name':'susan', 'active': False},
    {'name': 'bob', 'active': True}
    ]
"""

def filter_users(users):
    # Your code here
    return [user for