# conditional test added in 7-5
# break statement added in 7-5
# active variable in 7-6 (BELOW)

# set program status to active
active = True
# set prices for each tier of customer age
baby = {
    "cost": "free",
    "dollar": 0,
}
young = {
    "cost": "$10",
    "dollar": 10,
}
adult = {
    "cost": "$15",
    "dollar": 15,
}

# define the list group
group = []
# set the starting bill to 0
bill = 0

# ask user how many customers are in their party (which determines how
# many loops are needed)
group_num = int(input("How many in your group?\n:"))

# for loop that asks for age and then prints a ticket price based on
# the user's answer for each user in the group
# it also adds their price to the total for the group
for customer in range(group_num):
    age = input("Step right up! How old are you?\n:")
    # if the user types 'quit', the program ends
    if age == "quit":
        break
    # set 'age' to be an integer
    age = int(age)
    if age < 0:
        active = False
        print("You have broken the laws of physics, captain!")
    # if the user is less than 3, print them a message and return
    elif age < 3:
        print(f"Good news! Bebes get in for {baby['cost']}.")
        bill = bill + baby["dollar"]
    # else if they are 12 or under, print a message and return
    elif age < 13:
        print(f"Your ticket will be {young['cost']}.")
        bill = bill + young["dollar"]
    # if they are 13 or over, print a message
    elif age > 12:
        print(f"That's gonna be {adult['cost']}.")
        bill = bill + adult["dollar"]

print(f"\nOk, your total today will be ${bill}.\n")
