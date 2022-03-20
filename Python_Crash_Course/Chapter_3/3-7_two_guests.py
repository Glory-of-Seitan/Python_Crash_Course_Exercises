from operator import index, indexOf


guest_list = ["Hedy Lamarr", "Kelli Scheuble", "Carrie Fisher"]
# define 'guest_list


n = 0
cycles = 3
# set invitations to start at index[0]
# set number of passes through the list. A better way to do this would be to set equal to the number of entries on the list


for times in range(cycles):

    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a fascinating story with which to regale us."
    print(message)
    n = n + 1
# for loop that sends the same invitation to each guest on the list


print(
    f"\nUPDATE: Taco Bell has informed us that a larger dining table is available for reservation. Expect a second invite and more guests on the final guest list."
)

guest_list.insert(0, "Moose McLuckie")
guest_list.insert(2, "Ilana Glazer")
guest_list.append("Abbi Jacobsen")
# add 3 more guests to the list


n = 0
cycles = 6
# set starting index and number of loops

for times in range(cycles):

    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a fascinating story with which to regale us."
    print(message)
    n = n + 1
# re-run loop for the new list of 6


print(
    "\nDear all,\nUnfortunately, in a tragic turn of events, Taco Bell has had all their tables stolen in a rash of brazen thefts. They will only be able to provide stool and counter seating to myself and two guests. Those of you who are expendable will be receiving dis-invites shortly. Sorry for any inconvenience."
)
# tell guests they can't all come


n = 0
cycles = 4
# set invitations to start at index[0]
# set number of passes through the list. A better way to do this would be to set equal to the number of entries on the list

weak_links = ["Hedy Lamarr", "Ilana Glazer", "Carrie Fisher", "Abbi Jacobsen"]
    # define a list of guests to be uninvited

for times in range(cycles):
    # for loop that uninvites 4 people

    weakest_link = weak_links.pop(0)
    # pop the first value on 'weak_links' and set it to a variable

    i = guest_list.index(weakest_link)

    uninvited = guest_list.pop(i)
    # use that variable to pop a specific guest on the guest list

    message = f"\nDear {uninvited.title()}, I am sorry to inform you that you are the weakest link. Goodbye. there will be no tacos for you."
    print(message)
# tell the guest they are univited. Rudely.


n = 0
cycles = 2
# set starting index and number of loops

for times in range(cycles):
    # for loop that re-invites the remaining 2 guests
    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a fascinating story with which to regale us."
    print(message)
    n = n + 1
