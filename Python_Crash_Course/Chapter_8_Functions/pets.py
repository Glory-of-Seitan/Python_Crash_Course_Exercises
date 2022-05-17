def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("rufus", "dog")
describe_pet("captain", "capybara")
describe_pet(pet_name="rufus", animal_type="dog")
describe_pet("bingo")
describe_pet("thomas", "cat")
