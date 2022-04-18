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
    print(f"Adding {requested_topping}.")

print(
    "\nPizzaBot 9000 has finished making your pizza! Insert payment or be "
    "vaporized.\n"
)
