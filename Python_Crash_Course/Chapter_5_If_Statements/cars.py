# define list 'cars'
cars = ["audi", "bmw", "subaru", "toyota"]

# for loop printing each value in 'cars' with an if/else statment that
# capitalizes any value that == 'bmw'
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# this check will return FALSE
car = "audi"
car == "bmw"

# this check will return true
car = "audi"
car == "audi"

# this check will return false because capitalization matters
car = "audi"
car == "Audi"

# this gets around caps when it doesn't matter and returns TRUE
# this test is case insensitive as long as the letters are accurate
car = "Audi"
car.lower() == "audi"
# OR
car = "audi"
car.upper() == "AUDI"
# OR
car = "audi"
car.title() == "Audi"
