# # make cats.txt file and add names of 3 cats
# filename = "cats.txt"
# cats = ["scratchy", "emma", "tom"]
# with open(f"python_crash_course/txt_files/{filename}", "w") as file_object:
#     for cat in cats:
#         file_object.write(f"{cat.title()}\n")

# # make dogs.txt file and add names of 3 dogs
# filename = "dogs.txt"
# dogs = ["bingo", "spike", "lucy"]
# with open(f"python_crash_course/txt_files/{filename}", "w") as file_object:
#     for dog in dogs:
#         file_object.write(f"{dog.title()}\n")

# read these two files and print their contents to the screen
# use a try-except block to catch the FileNotFound error
filenames = ["cats.txt", "dogs.txt"]
for filename in filenames:
    try:
        with open(f"python_crash_course/txt_files/{filename}") as file_object:
            contents = file_object.read()
            print(f"Contents of {filename}: \n{contents}")
    except FileNotFoundError:
        pass
        # print a friendly message informing user
