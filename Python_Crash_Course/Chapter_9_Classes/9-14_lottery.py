from random import choice, randint

# make a list with 10 numbers and 5 letters on it for the possible
# lottery draw values
possible_values = list(range(0, 10))
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
]

# add the letters to the list of possible draws
for letter in letters:
    possible_values.append(letter)

# define the list that will include the winning draws
winners = []

# create a copy of the list of possible winners as a slice
# then we can pop() the winners off the list without destroying the orig
lott_balls = possible_values[:]
# for loop that will pop() a random value from lott_balls and
# append it to the list of winners. this happens 4 times
for draw in range(0, 4):
    winners.append(lott_balls.pop(randint(1, len(lott_balls) - 1)))

# print a message with the winning lottery numbers and
# congratulate the winners
print(
    f"\nAlright folks, this week's Mega Millions draw is over! "
    f"Anyone with a ticket matching the sequence:\n"
    f"'{winners[0]}-{winners[1]}-{winners[2]}-{winners[3]}'"
    f"\nIs now 1.6 million dollars richer! Come on down and get yer money.\n"
)
