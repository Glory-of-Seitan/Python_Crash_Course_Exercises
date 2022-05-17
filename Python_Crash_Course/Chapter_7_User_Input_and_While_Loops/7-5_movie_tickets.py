# set program status to active
active = True
# set prices for each tier of customer age
baby = "free"
young = "$10"
adult = "$15"

# while loop that asks for age and then prints a ticket price based on
# the user's answer
while active == True:
    age = input("Step right up! How old are you?\n:")
    # if the user types 'quit', the program ends
    if age == "quit":
        break
    # set 'age' to be an integer
    age = int(age)
    if age < 0:
        active = False
    # if the user is less than 3, print them a message and return
    elif age < 3:
        print(f"Good news! Bebes get in for {baby}.")
    # else if they are 12 or under, print a message and return
    elif age < 13:
        print(f"Your ticket will be {young}.")
    # if they are 13 or over, print a message
    elif age > 12:
        print(f"That's gonna be {adult}.")
