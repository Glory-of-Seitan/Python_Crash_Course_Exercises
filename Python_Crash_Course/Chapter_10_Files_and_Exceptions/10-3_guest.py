name = input("What is your name?:")

filename = 'guest.txt'
with open(f'python_crash_course/txt_files/{filename}', 'a') as file_object:
    file_object.write(f"\n{name}")
