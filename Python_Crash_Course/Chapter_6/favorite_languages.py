# define a dictionary of some people's favorite programming languages
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# print sarah's favorite language
# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite programming language is {language}.")


### ITERATING OVER THE DICTIONARY ###

# print a message for each person telling their favorite language
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")
print("")

# loop thru all the keys in 'favorite_languages' (all the names) and
# print each one
for name in favorite_languages.keys():
    print(name.title())


### LOOPING THRU AND PRINTING A MESSAGE IF FRIENDS ###
### HAVE A CERTAIN FAVORITE LANGUAGE ###

friends = [
    "phil",
    "sarah",
]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("\nErin, please take our poll! JOIN US. JOIN US ERIN.")


### LOOPING THRU A DICTIONARY IN A PARTICULAR ORDER ###

# loop through the names(keys) in the 'favorite_languages' dictionary
# thank them for taking the poll
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# print all the languages that people mentioned as their favorite in
# the dictionary 'favorite_languages'
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# use a set to print all the languages in favorite_languages w/o repeats
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


### USING NESTED LISTS WITHIN A DICTIONARY TO STORE MULTIPLE ###
### FAVORITE LANGUAGES PER PERSON (PER KEY) ###

# define the list of favorite language with the addition of java and
# an empty list for 'Julie'
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": "c",
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
    "dennis": ["java", "C++"],
    "Julie": [],
}

# for loop that checks if the person has 0, 1, or more comp languages
# and prints an appropriate message followed by the langauges
for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print(f"\n{name.title()}'s favorite languages are:")
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    elif len(languages) == 0:
        print(f"\n{name.title()} has no favorite language.")
    for language in languages:
        if language.lower() == "java":
            print(f"\tPython")
        elif language.lower() != "java":
            print(f"\t{language.title()}")
