car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

###


# define 3 lists of cars I want, don't want, and own. (NOT TRUE TO LIFE)
cars_wanted = ["tesla", "audi", "ferrari", "porsche", "toyota"]
cars_unwanted = ["ford", "nissan", "kia", "volkswagen", "chevrolet"]
cars_owned = ["toyota", "ford", "volkswagen", "audi", "chevrolet"]

# for loop that prints a message for each car I own depending on if I
# want it or not
print("")
for car in cars_owned:
    if car not in cars_wanted:
        print(f"I should really sell my {car.title()}.")
    if car in cars_wanted:
        print(f"I should keep my {car.title()}. It gets me from point A to "
               "point B.")
print("")

# for loop that prints a message about cars that I want depending on if
# I own them or not
print("")
for car in cars_wanted:
    if car in cars_owned:
        print(f"I should buy another {car.title()}, these things are great!")
    if car not in cars_owned:
        print(
            f"I should really buy a {car.title()}. Perhaps if I refinance "
            "my mortgage?"
        )
print("")
