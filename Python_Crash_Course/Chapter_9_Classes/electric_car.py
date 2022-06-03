### creating an electric car with new attributes in the ###
### sub class and printing its dictionary with pprint ###

import pprint


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
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

    def fill_gas_tank(self):
        """Print a message to inform the gas tank has been filled"""
        print(f"Your {self.get_desc_name()} now has a full gas tank.")


class ElectricCar(Car):
    """Represents aspects of a car but is specific to electric vehicles"""

    def __init__(self, make, model, year, battery_size = 75):
        """Initialize attributes of the parent class"""
        """Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank and can't be filled!")


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")



# make an electric car and check/manipulate its attributes
my_tesla = ElectricCar("tesla", "roadster", 2021)


# print(my_tesla.get_desc_name())
# my_tesla.increment_odometer(576)
# my_tesla.read_odometer()
# my_tesla.fill_gas_tank()
# pprint.pprint(vars(my_tesla))


# make a gas powered car and compare
my_car = Car(
    "ford",
    "GT",
    2013,
)

# make an electric car and check/manipulate its attributes
my_tesla1 = ElectricCar("tesla", "roadster", 2021)

# make an electric car
my_tesla2 = ElectricCar("tesla", "roadster", 2021, 100)

print(my_car.get_desc_name())
my_car.fill_gas_tank()
pprint.pprint(vars(my_car))


print(my_tesla.get_desc_name())
my_tesla1.battery.describe_battery()
my_tesla1.battery.get_range()

my_tesla2.battery.describe_battery()
my_tesla2.battery.get_range()