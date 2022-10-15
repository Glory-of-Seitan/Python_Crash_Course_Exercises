def make_shirt(size="large", text="i love python"):
    """Display information that should be printed on a custom t-shirt order"""
    print(f"You have ordered a size {size} shirt that says '{text.title()}'.")


make_shirt()
make_shirt("medium")
make_shirt(text="maybe a dingo ate your baby")
