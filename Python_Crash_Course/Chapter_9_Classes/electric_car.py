from car_module import Car


class ElectricCar(Car):
    """Represents aspects of a car but is specific to electric vehicles"""

    def __init__(self, make, model, year, battery_size=75):
        """Initialize attributes of the parent class"""
        """Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank and can't be filled!")


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
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

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
        elif self.battery_size == 100:
            print("This battery cannot be upgraded! It is already top of the line.")


my_car = ElectricCar(make = 'tesla', model = 'roadster', year = '1995')
print(my_car.odometer_reading)
print(my_car.make, my_car.model, my_car.year)