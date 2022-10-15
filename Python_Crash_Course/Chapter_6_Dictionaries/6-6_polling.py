# define the list of people who should take the favorite comp lang poll
poll_takers = [
    "kelli",
    "jen",
    "phil",
    "ned",
    "mike",
    "sarah",
    "john",
]

# define a dictionary of some people's favorite programming languages
favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "ruby",
    "phil": "python",
}
print("")
for taker in poll_takers:
    if taker in favorite_languages.keys():
        language = favorite_languages[taker]
        if language != "java":
            print(
                f"Thank you {taker.title()} for taking our poll. We enjoy {language} too!"
            )
        if language == "java":
            print(f"{taker.title()}, what the hell, dawg.")
    if taker not in favorite_languages.keys():
        print(f"Hey {taker.title()}, would you like take our poll?")
print("")
