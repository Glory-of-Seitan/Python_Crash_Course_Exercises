filename = 'Python_Crash_Course/txt_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# now do the same but for 1 million digits of Pi
filename = 'Python_Crash_Course/txt_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


birthday = input("Enter your birthday, in the form of mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi. Congrats.")
else:
    print("Your birthday does not appear in the first million digits of pi.")
