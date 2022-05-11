# set the program to active
active = True
# define the list of toppings that will be printed at the end
toppings = []

# initial message with instructions
topping = input(
    f"\nEnter your pizza toppings below\nEnter 'make' to finish or "
    f"'quit' to close \n: "
)
# adds the first topping to the list of toppings
toppings.append(topping)
print(f"\nWe're adding {topping} to your pizza now! *whirring noises*")

# while loop that asks the user for input - listing their toppings 1 by 1
while active == True:
    topping = input(
        f"\nEnter another pizza topping below OR\nEnter 'make' to finish or "
        f"'quit' to close \n: "
    )
    # if the user types 'quit' it leave the program
    if topping == "quit":
        break
    # if the user types 'make' it prints a message with all their toppings
    if topping == "make":
        print(f"Your pizza with {toppings} is being tossed in the oven now!")
        break
    # message announcing which topping was added in this go around the loop
    print(f"\nWe're adding {topping} to your pizza now *whirring noises*")
    # adds the topping to the list of toppings
    toppings.append(topping)
