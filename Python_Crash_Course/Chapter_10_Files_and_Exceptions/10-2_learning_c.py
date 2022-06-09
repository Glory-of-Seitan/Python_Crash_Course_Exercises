print("----------------------------------------------------------------------")
print("")

with open("Python_Crash_Course/txt_files/learning_python.txt") as file_object:
    contents = file_object.read()
    contents = contents.strip()
print(contents.replace("Python", "C"))

print("")
print("----------------------------------------------------------------------")
