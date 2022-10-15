guest_list = ["Hedy Lamarr", "Kelli Scheuble", "Tycho Brahe"]

n = 0
cycles = 3

for times in range(cycles):

    message = f"\nDear {guest_list[n].title()}, \nYou are cordially invited to dinner tonight at the Taco Bell over by the Shell Gas station. Bring your finest evening attire and a dozen of your closest friends.\nWe have only sent out {len(guest_list)} of these invitations, so consider yourselves lucky."
    print(message)
    n = n + 1
