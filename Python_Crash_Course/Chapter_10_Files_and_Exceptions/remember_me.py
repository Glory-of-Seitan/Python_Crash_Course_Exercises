import json


def get_stored_username():
    """Retrieve a stored username (if there is one)."""
    filename = "username.json"
    try:
        with open(f"Python_Crash_Course/json_files/{filename}") as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet the user by name if possible. If not, get their username and save it"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}. Where have you been all my life?")
    else:
        get_new_user()


def get_new_user():
    """Prompt for a username and store it in a .json file"""
    username = input("What is your name?:")
    filename = "username.json"
    with open(f"Python_crash_course/json_files/{filename}", "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back... {username}.")
    return username


greet_user()
