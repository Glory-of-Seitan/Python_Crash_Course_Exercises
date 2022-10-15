# sets the current number to 0
current_num = 0
# while loop that runs while the current number is less than 10
while current_num < 10:
    # increments the current number by one
    current_num += 1
    # if the current number is EVEN, continues without printing
    if current_num % 2 == 0:
        continue
    # prints the current number (should only reach here on odd nums)
    print(current_num)


### Avoiding infinite loops ###

#x this loop runs FOREVER!
x = 1
while x <= 5:
    print(x)