# define a function that greets someone based on their username
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")


# call the function and provide it a username as a parameter to use
greet_user("hercules")


########################################################################
### Using a Function with a while Loop (pg 141)
########################################################################

# function from 'formatted_name.py'
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
