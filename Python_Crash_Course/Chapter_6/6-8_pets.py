# define 3 dictionaries with information about various companions
rufus = {
    "name": "rufus",
    "breed": "shetland sheepdog",
    "human": "john",
}
abby = {
    "name": "abby",
    "breed": "gordon setter",
    "human": "bill",
}
muffin = {
    "name": "muffin",
    "breed": "mutt",
    "human": "sue",
}

# put the dictionaries into a list 'pets'
pets = [
    rufus,
    muffin,
    abby,
]

# loop through 'pets' and define each dictionary as 'pet'
for pet in pets:
    # set variable name to be the name of the companion capitalized
    name = pet["name"]
    # print a message announcing which companion is tied to the info
    print(f"\nInfo on {name.title()}:")
    # loop through each dictionary 'pet' individually and print all the
    # key value pairs
    for key, value in pet.items():
        print(f"\t{name.title()}'s {key} is {value.title()}.")
