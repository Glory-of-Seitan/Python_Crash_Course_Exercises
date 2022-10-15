filename = 'alice.txt'

try:
    with open(f"python_crash_course/txt_files/{filename}", encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"I am terribly sorry, the file {filename} could not be found.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
