# make 3 dictionaries defining 3 different aliens
alien_0 = {
    "color": "green",
    "points": 5,
}
alien_1 = {
    "color": "yellow",
    "points": 10,
}
alien_2 = {
    "color": "red",
    "points": 15,
}

# define the list 'aliens' to include our 3 dictionaries from above
aliens = [alien_0, alien_1, alien_2]

# for loop that prints each dictionary in the list 'aliens'
for alien in aliens:
    print(alien)


### AUTO-GENERATE A LIST OF ALIENS ###

# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {
        "color": "green",
        "points": 5,
        "speed": "slow",
    }
    aliens.append(new_alien)

# change any green aliens to yellow and any yellow aliens to red
# (in the first 3 on the list)
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# show the first 5 aliens on list 'aliens'
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
