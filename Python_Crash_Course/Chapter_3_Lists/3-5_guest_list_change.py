guest_list = ["Hedy Lamarr", "Kelli Scheuble", "Carrie Fisher"]
# define 'guest_list


n = 0
cycles = 3
# set invitations to start at index[0]
# set number of passes through the list. A better way to do this would be to set equal to the number of entries on the list


for times in range(cycles):

    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a dozen of your closest friends."
    print(message)
    n = n + 1
# for loop that sends the same invitation to each guest on the list


print(
    f"\nUnfortunately, {guest_list[0].title()} is unable to make it due to the outbreak of a new world war :( \nWe will be inviting a new guest and sending out a second round of invitations."
)
# a message indicating guest[0] couldn't make it and new invites will be sent


guest_list.insert(0, "Betty White")
# swap Hedy for Betty


n = 0
# redefine invitations to start at index[0]


for times in range(cycles):

    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a dozen of your closest friends."
    print(message)
    n = n + 1
# run the invite loop again
