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
        print(
            f"{self.name.title()} is a new restaurant that "
            f"serves {self.cuisine.title()} food."
        )

    def open_restaurant(self):
        """Informs that restaurant is open"""
        print(f"{self.name.title()} restaurant is open for business!")

    def set_num_served(self, num):
        """Sets the number of customers served to a given value"""
        self.num_served = num

    def increment_num_served(self, num_increment):
        """Adds a given value to the total customers served"""
        self.num_served += num_increment
