# define age
age = 31

# define messages as variables for quick use
baby_message = "Wow, you're still a baby. Life is all downhill from here."
toddler_message = "Here comes a toddler, watch out everybody!"
kid_message = (
    "Hey kid. Please stop trying to light my jeans on fire. We're"
    " trying to eat dinner here."
)
teen_message = "You're a teenager? Good luck."
adult_message = "You're an adult now. Your best days are already behind you."
elder_message = "You're over 65? Dang, you're old AF."

# if-elif-else chain that prints a different message at different
# stages of a human being's life depending on their age in years
if age < 2:
    print(f"\n{baby_message}\n")
elif age < 4:
    print(f"\n{toddler_message}\n")
elif age < 13:
    print(f"\n{kid_message}\n")
elif age < 20:
    print(f"\n{teen_message}\n")
elif age < 65:
    print(f"\n{adult_message}\n")
elif age >= 65:
    print(f"\n{elder_message}\n")
