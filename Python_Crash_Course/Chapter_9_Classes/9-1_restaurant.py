class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type of cuisine"""
        self.name = name
        self.cuisine = cuisine

    def desc_restaurant(self):
        """Describe a restaurant"""
        print(f"{self.name} is a new restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        """Informs that restaurant is open"""
        print(f"{self.name} restaurant is open for business!")


restaurant = Restaurant("Sluggo's", "American")
print(restaurant.name)
print(restaurant.cuisine)

restaurant.desc_restaurant()
restaurant.open_restaurant()
