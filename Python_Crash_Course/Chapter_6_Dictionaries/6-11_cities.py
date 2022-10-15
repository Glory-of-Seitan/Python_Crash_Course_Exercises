# define dictionary 'cities' using city names as the key
cities = {
    "portland": {
        "country": "the USA",
        "population": "2.2 million",
        "fact": "It is weird",
    },
    "tokyo": {
        "country": "japan",
        "population": "37.3 million",
        "fact": "It is the world's most populated metropolitan area",
    },
    "minneapolis": {
        "country": "the USA",
        "population": "3.0 million",
        "fact": "It has the most days with sub-freezing temps of any major US metro",
    },
}

# loop thru the cities in dict 'cities' and grab key-values with items()
for city, info in cities.items():
    # print a blank space
    print("")
    # print the name of the current city
    print(f"{city.title()}:\n")
    # loop thru the dictionary containing info about the current city
    for key, value in info.items():
        # if-elif chain that prints different messages for each
        # potential 'key' value in the city info dict
        if key == "country":
            print(f"\t{city.title()} is located in {value}.")
        elif key == "population":
            print(f"\tIts metro area contains around {value} human souls.")
        elif key == "fact":
            print(f"\tRandom Fact: {value}.")
