with open("Python_Crash_Course/txt_files/pi_digits.txt") as file_object:
    contents = file_object.read()
print(f"\n{contents.rstrip()}")

with open(
    f"/Users/John/Desktop/Professional/ComputerApps/"
    f"Github_Project_Repos/Python_Crash_Course_MAIN/"
    f"Python_Crash_Course_Exercises/Python_Crash_Course/txt_files/pi_digits.txt"
) as file_object:
    contents = file_object.read()
print(f"\n{contents}")

filename = "pi_digits.txt"
with open(f"python_crash_course/txt_files/{filename}") as file_object:
    for line in file_object:
        print(line.rstrip())


with open("Python_Crash_Course/txt_files/pi_digits.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    print(f"{line.rstrip()}")
