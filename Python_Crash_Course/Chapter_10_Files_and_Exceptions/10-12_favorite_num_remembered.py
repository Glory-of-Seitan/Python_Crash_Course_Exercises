import json

def get_fav_num():
    fav_num = input("What's your favorite number?")
    filename = 'favorite_number.json'
    with open(f"Python_crash_course/json_files/{filename}", 'w') as f:
        json.dump(fav_num, f)
        print(f"Your favorite number ({fav_num}) has been stored")


def read_fav_num():
    filename = 'favorite_number.json'
    try:
        with open(f"Python_crash_course/json_files/{filename}") as f:
            fav_num = json.load(f)
    except FileNotFoundError: 
        print("If you have a favorite number, we didn't find it :(")
        return None
    else:
        print(f"Your favorite number is ...drumroll... {fav_num}!")
        return(fav_num)

fav_num = read_fav_num()
if fav_num:
    pass
else:
    get_fav_num()
