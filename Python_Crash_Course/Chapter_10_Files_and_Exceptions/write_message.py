filename = 'programming.txt'

with open(f'python_crash_course/txt_files/{filename}', 'w') as file_object:
    file_object.write("I sure do love programming.\n")
    file_object.write("I love creating games.\n")

with open(f'python_crash_course/txt_files/{filename}', 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. What a rush!\n")
    file_object.write("I love creating apps that can run in a browser.\n")
