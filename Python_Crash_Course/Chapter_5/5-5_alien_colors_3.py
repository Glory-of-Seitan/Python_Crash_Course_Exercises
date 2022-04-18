# define color of alien killed
alien_color = "red"

# define kill messages for 3 types of alien
green_kill = "You just shot down a green alien. That's worth 5 POINTS!"
yellow_kill = "You just shot down a yellow alien. That's worth 10 POINTS!"
red_kill = "You just shot down a red alien. That's worth 15 POINTS!"

# if-elif-else chain that checks what color the killed alien was and
# prints a message awarding pts accordingly
if alien_color == "green":
    print(f"\n{green_kill}\n")
elif alien_color == "yellow":
    print(f"\n{yellow_kill}\n")
elif alien_color == "red":
    print(f"\n{red_kill}\n")
