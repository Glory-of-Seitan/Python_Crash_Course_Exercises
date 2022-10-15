# already had made the print calls into a loop, here have just
# added 5 more terms to the dictionary in 6-3

# define a short glossary of coding terms in a dictionary 'code_glossary'
code_glossary = {
    "slice": "A section of a list that you can choose to work with by defining "
    "index numbers.",
    "list": "A list is a series of values stored in " "a single variable.",
    "dictionary": "Dictionaries are used to store data values in "
    "key:value pairs. A dictionary is a collection which is ordered, "
    "changeable and does not allow duplicates.",
    "list comprehension": "List comprehension offers a shorter syntax when you "
    "want to create a new list based on the values of "
    "an existing list.",
    "variable": "Variables are containers for storing data values.",
    "shell": "In computing, a shell is a computer program which exposes an "
    "operating system's services to a human user or other programs. In "
    "general, operating system shells use either a command-line interface "
    "(CLI) or graphical user interface (GUI), depending on a computer's role "
    "and particular operation. It is named a shell because it is the outermost "
    "layer around the operating system.",
    "compiler": "a program that converts instructions into a machine-code or "
    "lower-level form so that they can be read and executed by a computer.",
    "argument": "An argument is a way to provide more information to a "
    "function. The function can then use that information as it runs, like a "
    "variable.",
    "array": "Arrays are containers that hold variables; they're used to group "
    "together similar variables. You can think of arrays like shelves at a pet "
    "store. The array would be the shelf, and the animals in cages are the "
    "variables inside (kind of a weird example tho).",
    "statement": "The way you tell a computer to perform an action is by giving "
    "it instructions or writing statements to explain a desired action. Again, "
    "it’s similar to writing sentences in English, but with words, numbers, and "
    "punctuation added depending on the programming language.",
}

# a for loop that prints each key value and its definition in an easy
# to read format
print("\n")
for i in code_glossary:
    print(f"{i}: \n{code_glossary[i]}\n")
