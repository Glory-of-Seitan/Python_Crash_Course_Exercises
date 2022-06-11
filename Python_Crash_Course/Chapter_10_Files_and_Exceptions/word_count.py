def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(f"python_crash_course/txt_files/{filename}", encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"I am terribly sorry, the file {filename} could not be found.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = "pride_and_prejudice.txt"
count_words(filename)

filenames = [
    "alice.txt",
    "lord_of_the_flies.txt",
    "moby_dick.txt",
    "little_women.txt",
]
for filename in filenames:
    count_words(filename)
