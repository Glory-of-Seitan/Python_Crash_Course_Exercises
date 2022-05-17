squares = []
# make empty list 'squares'

for value in range(1, 11):
    squares.append(value**2)
# a loop that will execute 10 times starting at 1
# each iteration will calculate the square of the value and append it to our 'squares' list

print(squares)
# print the finished list


###list comprehension below

squares = [value**2 for value in range(1, 11)]
print(squares)
# list comprehension that does the same thing as lines 1-9
