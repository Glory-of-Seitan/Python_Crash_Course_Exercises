friends = ["Radish", "Abbi", "Karin", "David"]
# define list of friends
i = 0
# set variable to first index
greeting = f"Good morning {friends[i].title()}. Would you like to play a game?"
# define 'greeting' to include the first index

print(greeting)

i = i + 1
# set 'i' to be the next index in the list

greeting = f"Good morning {friends[i].title()}. Would you like to play a game?"
# redefine 'greeting' to choose the next name on the list (using the new 'i')

print(greeting)

# print and keep repeating the process. obviously a FOR loop would be a better choice, but that's later in the book.

i = i + 1
greeting = f"Good morning {friends[i].title()}. Would you like to play a game?"
print(greeting)

i = i + 1
greeting = f"Good morning {friends[i].title()}. Would you like to play a game?"
print(greeting)
