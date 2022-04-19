# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#    print("Hold the anchovies!")

# define the list of requested toppings
requested_toppings = ["mushrooms", "onions"]

# print a starting message and if statements checking for each topping
# each successful check prints a message that the topping is being added
print("\nPizzaBot 9000 beginning pizza sequence #1 with your requested toppings." "\n")
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "onions" in requested_toppings:
    print("Adding onions.")
if "pineapple" in requested_toppings:
    print("Adding pineapple.")

# print message that the pizza is finished and the choice is payment
# or death
print(
    "\nPizzaBot 9000 has finished making your pizza! Insert payment or be "
    "vaporized.\n"
)

### CHECKING FOR SPECIAL ITEMS ###

requested_toppings = [
    "mushrooms",
    "green peppers",
    "extra cheeze",
    "pineapple",
    "bbq chikn",
]

print("\nPizzaBot 9000 beginning pizza sequence #2 with your requested toppings." "\n")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now and forever.")
    else:
        print(f"Adding {requested_topping}.")

print(
    "\nPizzaBot 9000 has finished making your pizza! Insert payment or be "
    "vaporized.\n"
)


### CHECKING THAT A LIST IS NOT EMPTY ###

# define requested_toppings as empty
requested_toppings = []

# if requested_toppings is not empty, this will return TRUE and it will
# execute the for loop from above
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers right now and forever.")
        else:
            print(f"Adding {requested_topping}.")
# if requested toppings is empty, it will skip the for loop and print
# this message
else:
    print("Are you sure you want a plain pizza? Weirdo.")


### USING MULTIPLE LISTS ###

#list to define the available toppings from which customers can choose
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

#list to define the toppings for which a customer asked
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

#message that pizza-making is starting
print("\nPizzaBot 9000 beginning pizza sequence with your requested toppings." "\n")

#for loop to print requested toppings that are available
#and inform customers when a requested topping is unavailable
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}. In fact, that's kind of a "
               "weird one to ask for. *looks at you like you're weird*")

#print a message that pizza is finished
print(
    "\nPizzaBot 9000 has finished making your pizza! Insert payment or be "
    "vaporized.\n"
)