class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and type of cuisine"""
        self.name = name
        self.cuisine = cuisine

    def desc_restaurant(self):
        """Describe a restaurant"""
        print(f"{self.name} is a restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        """Informs that restaurant is open"""
        print(f"{self.name} restaurant is open for business!")


restr_1 = Restaurant("Kung POW!", "Chinese")
restr_2 = Restaurant("Epif", "South American")
restr_3 = Restaurant("Enat", "Ethiopian")

restr_1.desc_restaurant()
restr_2.desc_restaurant()
restr_3.desc_restaurant()
