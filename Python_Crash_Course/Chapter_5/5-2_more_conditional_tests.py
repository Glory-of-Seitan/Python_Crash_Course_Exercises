#create 2 lists of the multiples of 7 and 8, respectively
mults_of_seven = [value for value in range(7,1001,7)]
mults_of_eight = [value for value in range(8,1001,8)]
double_mults = []

#for loop that checks if a multiple of 8 is also a multiple of 7
print("\nFor numbers between 1 and 1000, these are the multiples of eight that"
      " are also multiples of seven:\n")
for mult_eight in mults_of_eight:
    if mult_eight in mults_of_seven:
        double_mults.append(mult_eight)
print(double_mults)
#define 'double_sum' to be the sum of all numbers that are multiples of 7&8
#between 1 and 1000
double_sum = sum(double_mults)

#numerical tests on above lists
print('')
print(f"Is 688 a multiple of eight? = {688 in mults_of_eight}")
print(f"Is 688 a multiple of seven? = {688 in mults_of_seven}")
print(f"Is 685 a multiple of eight? = {685 in mults_of_eight}")
print(f"Is 167,000 greater than the sum of the "
      f"multiples of eight between one and 1000? = "
      f"{167000 > sum(mults_of_eight)}")
print(f"The sum of the multiples of eight is = {sum(mults_of_eight)}")
print(f"Is 71,500 less than the sum of the "
      f"multiples of seven between one and 1000?"
      f" = {71500 < sum(mults_of_seven)}")
print(f"The sum of the multiples of 7 between 1-1000 is {sum(mults_of_seven)}")
print(f"Is 672 a multiple of both 7 and 8? = {672 in double_mults}.")
print(f"Is 688 a multiple of both 7 and 8? = {688 in double_mults}.")
print(f"Is 10,052 greater than or equal to the sum of double_mults? "
      f"= {10052 >= double_sum}")
print(f"Is 7,507 greater than or equal to the sum of double_mults? "
      f"= {7507 >= double_sum}")
print(f"Is 8,568 less than or equal to the sum of double_mults? "
      f"= {8568 <= double_sum}")
print(f"The sum of double_mults is {double_sum}.")
print('')


###


# define 3 lists of cars I want, don't want, and own. (NOT TRUE TO LIFE)
cars_wanted = ["tesla", "audi", "ferrari", "porsche", "toyota"]
cars_unwanted = ["ford", "nissan", "kia", "volkswagen", "chevrolet"]
cars_owned = ["toyota", "ford", "volkswagen", "audi", "chevrolet"]

#checking if an item is in a list
print("These are the cars I want to keep:")
for car in cars_owned:
    if car in cars_wanted:
        print(car)

cars_owned.insert(0, cars_owned[0].title())