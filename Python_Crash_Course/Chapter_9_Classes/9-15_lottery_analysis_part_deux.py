from random import choice, randint
from statistics import mean

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
# define the ticket that stops the loop when it is drawn
my_ticket = [1, 2, 3, 4]

# create a copy of the list of possible winners as a slice
# then we can pop() the winners off the list without destroying the orig
lott_balls = possible_values[:]

# define the list that will include the total_draws upon each win
# these are to be averaged
total_draws_on_wins = []

# for loop that will pop() a random value from lott_balls and
# append it to the list of winners. this happens 4 times
for time in range(0, 100):
    # set total draws to 0
    total_draws = 0
    winners = []
    while winners != my_ticket:
        for draw in range(0, 4):
            winners.append(lott_balls.pop(randint(1, len(lott_balls) - 1)))
        if winners == my_ticket:
            total_draws_on_wins.append(total_draws)
            break
        else:
            winners = []
            total_draws += 1
            lott_balls = possible_values[:]
            print(f"Total draws so far -{total_draws}")
    # print the total draws it took for 1,2,3,4 to win
    print(
        f"\nIt took {total_draws} total draws for your ticket to win. "
        f"This is why no one should play the lottery"
    )


# print a message with the winning lottery numbers and
# congratulate the winners
total_average = mean(total_draws_on_wins)
print(total_draws_on_wins)
print(
    f"\nOn average, over 100 attempts, it took {total_average} rounds "
    f"for your chosen ticket to be the winner each time."
)
