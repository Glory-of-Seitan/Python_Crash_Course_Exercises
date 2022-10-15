# define list of current users
current_users = ["John", "Kelli", "cat", "dog", "admin"]
# define list of users to be added
new_users = ["kaylA", "radish", "Admin", "cAt", "dave"]

current_users_lower = [x.lower() for x in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"\nI'm sorry, the username '{new_user.title()}' is taken. "
            "You'll have to choose a new one."
        )
    else:
        print(f"\n{new_user.title()}: This username is available.")
print()
