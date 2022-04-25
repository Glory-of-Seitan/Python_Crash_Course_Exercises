# define a dictionary that stores 5 people's favorite numbers
# print each person's name and their favorite number
# is there a way to iterate through the dictionary and do this?
# look ahead in the book
friend_numbers = {
    "radish": 0,
    "kelli": 100,
    "abbi": 88,
    "David": 2,
    "Fin": 1
}

#print the dictionary 'friend_numbers'
print(friend_numbers)

# for loop that prints 'friend_numbers' in a much nicer way
for i in friend_numbers:
    print(i, friend_numbers[i])