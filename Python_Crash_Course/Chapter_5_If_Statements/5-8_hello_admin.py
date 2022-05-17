# define the list of users
users = ["john", "kelli", "dog", "admin", "cat"]

# for loop that checks if the user is the admin and prints a special
# message if they are. Otherwise it prints a generic greeting
print()
for user in users:
    if user == "admin":
        print(
            "Hello to the most important person of all. Would you like to "
            "see a status report?"
        )
    else:
        print(f"Hello {user.title()}, thank you for logging in.")
print()
