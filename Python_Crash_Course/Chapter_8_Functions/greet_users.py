def greet_users(names):
    """Print a sipmle greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot',]
greet_users(usernames)