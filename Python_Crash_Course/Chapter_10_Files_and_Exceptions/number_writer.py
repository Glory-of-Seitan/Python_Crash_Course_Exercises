import json

numbers = [2, 4, 67, 5, 1, 1000]

filename = 'numbers.json'
with open(f"Python_Crash_Course/json_files/{filename}", 'w') as f:
    json.dump(numbers, f)
