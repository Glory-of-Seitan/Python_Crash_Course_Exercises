# define a dictionary that contains the names of 3 major rivers and
# their corresponding nations
world_rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "usa",
}

# print the rivers
print("\nHere are some major world rivers:")
for river in world_rivers:
    print(river.title())

# print the countries
print("\nHere are the countries within which these rivers flow:")
for country in world_rivers.values():
    if country.lower() != "usa":
        print(country.title())
    if country.lower() == "usa":
        print(f"The {country.upper()}")

# print a message connecting the rivers with their countries
print("")
for river in world_rivers:
    country = world_rivers[river]
    if country != "usa":
        print(f"The {river.title()} runs through {country.title()}.")
    if country == "usa":
        print(f"The {river.title()} runs through the {country.upper()}.")
print("")
