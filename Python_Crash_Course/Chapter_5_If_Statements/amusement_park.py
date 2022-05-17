age = 12
if age < 4:
    print("Your admission cost is $0.")  # toddlers and bebes
elif age < 18:
    print("Your admission cost is $25.")  # kids
elif age < 65:
    print("Your admission cost is $40.")  # full adult
else:
    print("Your admission cost is $20")  # seniors

    ### More efficient way below ###
    ### Only the variable changes ###

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# in addition to being more efficient, this revised code is easier to
# modify than the original approach. To change the text of the output
# message, you would need to change only one print() call rather than
# three separate print() calls. At scale, those changes would be tedious
