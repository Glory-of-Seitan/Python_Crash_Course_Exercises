# define the dictionary 'favorite_places' with names as the key
# and a list of their favorite places as the value
favorite_places = {
    "jimbo": [
        "the lake",
        "maruti",
        "home",
    ],
    "kati": [
        "the three sisters",
        "mt hood",
        "bend",
    ],
    "rufus": [
        "the park",
        "the backyard",
        "the car",
    ],
}

# loop thru 'favorite_places' with items() and print a message
# announcing the person
for person, places in favorite_places.items():
    print(f"Some of {person.title()}'s favorite places include:")
    # loop thru places and print each place on a new line
    for place in places:
        print(f"\t{place.title()}")
