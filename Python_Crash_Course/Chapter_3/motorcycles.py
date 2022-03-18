motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# define list 'motorcycles'
# print

motorcycles[0] = "ducati"
print(motorcycles)
# change index [0] to 'ducati', deleting 'honda'
# print


###2nd Part###


motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# define list 'motorcycles'
# print

motorcycles.append("ducati")
print(motorcycles)
# append 'ducati' onto the end of list 'motorcycles'
# print


###3rd Part###


motorcycles = []
# define empty list 'motorcycles'

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
# add in values 1 by 1

print(motorcycles)
# print

message = "Hey is that a"
print(f"{message} {motorcycles[0].title()}?")
# define message to ask about motorcycle
# print the message along with a selected make as a question

motorcycles.insert(1, "ducati")
print(motorcycles)
# insert 'ducati' as a value in index[1]
# print


###4th Part###


motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# define list
# print


del motorcycles[1]
print(motorcycles)
# delete 1st value
# print


###5th Part###


motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# define list
# print


popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)
# pop out the value at index[1]
# print the list 'motorcycles' minus the popped value
# print the popped value


print(f"The last bike I owned was a {popped_motorcycles.title()}.")
# print a statement using the popped value


###6th Part###


motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
# define list
# print

motorcycles.remove("ducati")
print(motorcycles)
# remove 'ducati' value from list
# print

###7th Part###


motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
# define list
# print


too_expensive = "ducati"
motorcycles.remove(too_expensive)
# define 'ducati' as being too expensive (variable)
# remove that variable from the list 'motorcycles'

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.\n")
# print updated 'motorcycles with 'too_expensive' removed
# print a message explaining which brand was too expensive
