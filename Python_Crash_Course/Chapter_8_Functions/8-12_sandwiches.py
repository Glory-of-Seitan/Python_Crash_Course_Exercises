def make_sando(*toppings):
    """Summary of a sandwich order"""
    print(f"\nYou ordered a sandwich with these toppings: ")
    for topping in toppings:
        print(f" - {topping}")


make_sando(
    "red peppers",
    "tofurky",
    "chipotle aioli",
)
make_sando(
    "lettuce",
    "hummus",
    "sauerkraut",
)
make_sando(
    "tempeh",
    "bbq sauce",
    "spinach",
    "buffalo spread",
)
