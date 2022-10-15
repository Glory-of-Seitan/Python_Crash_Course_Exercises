# define 3 dictionaries holding info about each person
kelli = {
    "first name": "kati",
    "last name": "scramble",
    "age": 26,
    "city": "Gresham",
}

jonny = {
    "first name": "jonny",
    "last name": "crimble",
    "age": 31,
    "city": "minneapolis",
}

radish = {
    "first name": "radish",
    "last name": "XvX",
    "age": 29,
    "city": "Portland",
}

# put all 3 dictionaries above into the list 'people'
people = [kelli, jonny, radish]

# loop thru and print all the info about the people in 'people'
for person in people:
    # define first and last names of each person as variables so they
    # can be printed with title()
    first = person["first name"]
    last = person["last name"]
    # message on whose information is being printed
    print(f"\nInfo on {first.title()} {last.title()}:")
    # loop through the keys and values in each person's dictionary
    for key, value in person.items():
        # check if the value is an integer. If so, print normally
        if isinstance(value, int):
            print(f"\t{first.title()}'s {key} is {value}.")
        # check if the value is a string. If so, print with .title()
        if type(value) == str:
            print(f"\t{first.title()}'s {key} is {value.title()}.")
