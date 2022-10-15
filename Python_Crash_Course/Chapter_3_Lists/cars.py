cars = ["bmw", "audi", "subaru", "toyota"]
# define list 'cars'

cars.sort(reverse=True)
# sort cars in reverse alphabetical order

print("Here is the original list:")
print(cars)
# print list 'cars' reversed

print("\nHere is the sorted list:")
print(sorted(cars))
# print sorted 'cars'

print("\nHere is the original list again:")
print(cars)
# print the original reversed list again to prove that sorted() function doesn't alter or delete values

###Part 2###

cars = ["bmw", "audi", "subaru", "toyota"]
print(cars)
# define list 'cars' and print

cars.reverse()
print(cars)
# reverse() the list and print

len(cars)
