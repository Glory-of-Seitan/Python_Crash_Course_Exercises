import json

def get_fav_num():
    fav_num = input("What's your favorite number?")
    filename = 'favorite_number.json'
    with open(f"Python_crash_course/json_files/{filename}", 'w') as f:
        json.dump(fav_num, f)
        print(f"Your favorite number ({fav_num}) has been stored")

get_fav_num()