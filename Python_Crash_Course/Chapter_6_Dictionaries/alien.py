# define dictionary 'alien_0' and print both values by calling their
# key values in the print function
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# add values for x_position and y_position to the dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25

# define dictionary 'alien_1' as empty and then add color and points
# key values before printing
alien_1 = {}
alien_1["color"] = "red"
alien_1["points"] = 10
print(alien_1)

# change alien_1's color from 'red' to 'blue' and print a message
alien_1["color"] = "blue"
print(f"Alien 1 is now {alien_1['color']}.")


### TRACKING POSITION ###

# define dictionary 'alien_0' with original position and speed of the
# alien and print the x_position with a message
alien_0["x_position"] = 0
alien_0["y_position"] = 25 
alien_0["speed"] = "medium"
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")
# every time this code runs the alien will move either 1,2, or 3
# to the right (the x_position value will increase and be saved
# in the dictionary)

#delete the key value 'points' from alien_0 and check that it's gone
del alien_0['points']
print(alien_0)