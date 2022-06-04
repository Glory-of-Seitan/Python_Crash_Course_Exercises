from car_module import Car
from electric_car import ElectricCar as EC

# this method is not recommended because it can create issues
# it is unclear which classes the module is using
# it can cause conflicts if you accidentally import a class
# with the same name as something in your file
# it is better to name the classes you are using for clarity


my_beetle = Car("volkswagon", "beetle", 1972)
print(my_beetle.get_desc_name())

my_tesla = EC("tesla", "roadster", 2018, 100)
print(my_tesla.get_desc_name())
my_tesla.battery.get_range()
