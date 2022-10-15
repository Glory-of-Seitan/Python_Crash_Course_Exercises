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
        print(f"{self.name} is a new restaurant that serves {self.cuisine} food.")

    def open_restaurant(self):
        """Informs that restaurant is open"""
        print(f"{self.name} restaurant is open for business!")

    def set_num_served(self, num):
        """Sets the number of customers served to a given value"""
        self.num_served = num

    def increment_num_served(self, num_increment):
        """Adds a given value to the total customers served"""
        self.num_served += num_increment


# create a new instance of a restaurant
restaurant = Restaurant("Sluggo's", "American")

# print the restaurant name and type of food
print(restaurant.name)
print(restaurant.cuisine)

# print the starting number of customers served for the day
print(restaurant.num_served)

# set the customer count to 159 and print again
restaurant.num_served = 159
print(restaurant.num_served)

# increment the customer count by 100 and print again
restaurant.increment_num_served(100)
print(restaurant.num_served)
