# the color of alien killed
alien_color = "red"

# defines the kill messages for various aliens
green_kill = "You just shot down a green alien. That's worth 5 POINTS!"
other_kill = "You shot down a non-green alien. That's worth 10 POINTS!"

# tests if alien was green and awards 5 pts. if not, awards 10 pts. ELSE
# prints a message awarding 5 pts for green and 10 pts for anything else
if alien_color.lower() == "green":
    print(f"\n{green_kill}\n")
else:
    print(f"\n{other_kill}\n")

# tests if alien was green or otherwise but using the IF block
# prints the same messages as before
if alien_color.lower() == "green":
    print(f"\n{green_kill}\n")
if alien_color.lower() == "red":
    print(f"\n{other_kill}\n")
if alien_color.lower() == "yellow":
    print(f"\n{other_kill}\n")


### NOTES ###

# the if-else version prints the {other_kill} message no matter what
# the alien_color value is

# the if series version only prints the messages for the specified
# values. Anything else and it will have no output.
