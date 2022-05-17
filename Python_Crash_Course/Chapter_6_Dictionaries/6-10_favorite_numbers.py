# define dictionary 'friend numbers to include people and their
# favorite numbers (multiple)

friend_numbers = {
    "radish": [0, 6],
    "kelli": [
        100,
        69,
    ],
    "abbi": [
        88,
        3,
    ],
    "David": [2],
    "Fin": [1],
    "Joe": [],
}

# print the dictionary 'friend_numbers'
print(friend_numbers)

# for loop that grabs 'friend' (their name) and 'nums' (their favorite
# numbers)
# prints a message depending on how many values are in list 'nums'
# and then prints 'nums' if they have 1 or more
for friend, nums in friend_numbers.items():
    if len(nums) >= 2:
        print(f"{friend.title()}'s favorite numbers include:\n\t{nums}")
    elif len(nums) == 1:
        print(f"{friend.title()}'s favorite number is:\n\t{nums}")
    elif len(nums) == 0:
        print(f"{friend.title()} doesn't have a favorite number.")
