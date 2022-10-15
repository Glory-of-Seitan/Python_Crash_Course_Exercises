from car_module import ElectricCar 

my_tesla = ElectricCar("tesla", "model S", "2021", 100)
print(f"\n{my_tesla.get_desc_name()}")
my_tesla.odometer_reading = 320
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()