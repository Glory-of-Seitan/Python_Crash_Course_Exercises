import json


def greet_user():
    """Greet the user by name if possible. If not, get their username and save it"""
    username = get_stored_username()
    if username:
        answer = input(
            f"Welcome back, {username}... this is {username}, correct?\nY/N:"
        )
        if answer.lower() == "y":
            print("Ah, splendid. I knew it was you.")
        if answer.lower() == "n":
            get_new_user()
    else:
        get_new_user()


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


def get_new_user():
    """Prompt for a username and store it in a .json file"""
    username = input("What is your name?:")
    filename = "username.json"
    with open(f"Python_crash_course/json_files/{filename}", "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back... {username}.")
    return username


greet_user()
