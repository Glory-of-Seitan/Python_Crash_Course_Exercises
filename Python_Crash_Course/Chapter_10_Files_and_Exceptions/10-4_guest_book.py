filename = 'guest_book.txt'

print("Enter 'quit' at any time to exit")

while True:
    name = input("What is your name?:")
    if name.lower() == 'quit':
        break
    else:
        with open(f'python_crash_course/txt_files/{filename}', 'a') as file_object:
            file_object.write(f"\n{name}")
        print(f"Thank you for signing the guestbook, {name}.")
