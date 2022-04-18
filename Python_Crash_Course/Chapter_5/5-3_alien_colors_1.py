#version that succeeds - checks if a green alien was shot down and 
# prints a message informing user how many points it was worth
alien_color = 'green'
if alien_color == 'green':
    print("\nYou just shot down a green alien. That's worth 5 POINTS!\n")


#version that fails
alien_color = 'red'
if alien_color == 'green':
    print("\nYou just shot down a green alien. That's worth 5 POINTS!\n")