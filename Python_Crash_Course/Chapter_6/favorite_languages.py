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

friends = ["phil", 'sarah',]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll! JOIN US. JOIN US ERIN.")


### LOOPING THRU A DICTIONARY IN A PARTICULAR ORDER ###

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())