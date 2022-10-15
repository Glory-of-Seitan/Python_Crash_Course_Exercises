b_foods = ("rice", "beans", "tots", "guacamole", "ketchup")
# define tuple "b_foods"

for food in b_foods:
    print(food)
# for loop to print all values in 'b_foods'

b_foods[2] = "nachos"
# try to alter one value of 'b_foods'. this fails because tuples are
# immutable

b_foods = ("rice", "curly fries", "waffle fries", "guacamole", "ketchup")
# redefine the variable 'b_foods' to a new tuple with 2 changes

for food in b_foods:
    print(food)
# loop that prints all values in 'b_foods' again
