from car_module import Car, ElectricCar

my_new_car = Car("audi", "a4", 2017)
print(f"\n{my_new_car.get_desc_name()}")

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

