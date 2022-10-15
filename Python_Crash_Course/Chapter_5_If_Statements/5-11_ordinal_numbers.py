ord_nums = [x for x in range(1, 10)]

suf = "x"

for num in ord_nums:
    if num == 1:
        suf = "st"
    elif num == 2:
        suf = "nd"
    elif num == 3:
        suf = "rd"
    elif num > 3:
        suf = "th"
    else:
        print(f"{num} is not a valid input, please enter a number between 1 and 9.")
    print(f"{num}{suf}")
