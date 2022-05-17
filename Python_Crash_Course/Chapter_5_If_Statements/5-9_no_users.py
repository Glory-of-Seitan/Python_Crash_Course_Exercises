# define the list of users
users = []

# for loop that checks if the user is the admin and prints a special
# message if they are. Otherwise it prints a generic greeting
print()
if users:
    for user in users:
        if user == "admin":
            print(
                "Hello to the most important person of all. Would you like to "
                "see a status report?"
            )
        else:
            print(f"Hello {user.title()}, thank you for logging in.")
else:
    print("We need to find more users!")
print()
