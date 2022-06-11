filenames = [
    "alice.txt",
    "lord_of_the_flies.txt",
    "moby_dick.txt",
    "little_women.txt",
    "pride_and_prejudice.txt",
]

def count_the_thes(text):
    the_num = text.count('the')
    return the_num

def count_the_thes_acc(text):
    the_real_num = text.count('the ')
    return the_real_num

for filename in filenames:
    try:
        with open(f'python_crash_course/txt_files/{filename}') as f:
            contents = f.read()
            contents = contents.lower()
            print(f"\nHere's the number of times 'the' shows up in {filename}:\n{count_the_thes(contents)}")
            print(f"Here's the number of times the word 'the' shows up in {filename}:\n{count_the_thes_acc(contents)}")
    except FileNotFoundError:
        pass
