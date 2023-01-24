"""A class that can be used to represent a car"""


class Car:
    """A simple attempt to represent a car"""

    def __init__(
        self,
        make,
        model,
        year,
    ):
        """Initialize the attributes that describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desc_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement of the car's total mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to a new number"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("It's illegal to roll back an odometer!")

    def increment_odometer(self, miles):
        """Adds a given value to the current odometer reading"""
        self.odometer_reading += miles
