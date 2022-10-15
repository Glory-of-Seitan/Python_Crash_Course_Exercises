import json

def read_fav_num():
    filename = 'favorite_number.json'
    try:
        with open(f"Python_crash_course/json_files/{filename}") as f:
            fav_num = json.load(f)
    except FileNotFoundError: 
        print("If you have a favorite number, we didn't find it :(")
        return None
    else:
        return fav_num

print(f"Your favorite number is ...drumroll... {read_fav_num()}!")
