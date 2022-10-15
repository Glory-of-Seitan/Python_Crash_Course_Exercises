# define the class 'Restaurant' with a number of functions describing it
class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type of cuisine"""
        self.name = name
        self.cuisine = cuisine
        self.num_served = 0

    def desc_restaurant(self):
        """Describe a restaurant"""
        print(f"\n{self.name} is a new restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        """Informs that restaurant is open"""
        print(f"\n{self.name} restaurant is open for business!")

    def set_num_served(self, num):
        """Sets the number of customers served to a given value"""
        self.num_served = num

    def increment_num_served(self, num_increment):
        """Adds a given value to the total customers served"""
        self.num_served += num_increment


class IceCreamStand(Restaurant):
    """An attempt to model an ice cream stand as a subclass of Restaurant"""

    def __init__(self, name, flavors=[], cuisine="ice cream"):
        """Initialize an ice cream stand using Restaurant's __init__ and 'flavors'"""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def show_flavors(self):
        """Prints the flavors available at an ice cream stand"""
        print("\nFlavors Currently Available:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")


fifty_licks = IceCreamStand(
    "Fifty Licks",
    [
        "lemon saffron",
        "bananas foster",
        "chocolate",
    ],
)

fifty_licks.desc_restaurant()
fifty_licks.open_restaurant()
fifty_licks.show_flavors()
