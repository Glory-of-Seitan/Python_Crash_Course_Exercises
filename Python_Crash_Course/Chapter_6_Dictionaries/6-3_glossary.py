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
}

# a for loop that prints each key value and its definition in an easy
# to read format
print("\n")
for i in code_glossary:
    print(f"{i}: \n{code_glossary[i]}\n")
