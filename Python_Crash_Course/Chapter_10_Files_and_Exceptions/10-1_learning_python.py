print("----------------------------------------------------------------------")

# first printing
with open("Python_Crash_Course/txt_files/learning_python.txt") as file_object:
    contents = file_object.read()
print(f"{contents.rstrip()}")

print("----------------------------------------------------------------------")
# second printing
with open("Python_Crash_Course/txt_files/learning_python.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


print("----------------------------------------------------------------------")
# third printing
with open("Python_Crash_Course/txt_files/learning_python.txt") as file_object:
    lines = file_object.readlines()

learn_py_lines = []
for line in lines:
    learn_py_lines.append(line.rstrip())
for line in learn_py_lines:
    print(line)

print("----------------------------------------------------------------------")
