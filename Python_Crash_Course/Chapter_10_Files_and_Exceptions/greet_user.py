import json

filename = 'username.json'

with open(f"Python_Crash_Course/json_files/{filename}") as f:
    username = json.load(f)
    print(f"Welcome back, Commander {username}.")
