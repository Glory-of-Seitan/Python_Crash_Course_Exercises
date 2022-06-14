import json

filename = 'numbers.json'
with open(f"Python_Crash_Course/json_files/{filename}") as f:
    numbers = json.load(f)

print(numbers)
