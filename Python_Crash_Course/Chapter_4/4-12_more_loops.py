my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
# create a (disturbingly accurate) list of favorite foods for me and a friend. The friend's list is a slice containing everything in my list

print(f"\nMy favorite foods are:\n{my_foods}")
print(f"\nMy friend's favorite foods are:\n{friend_foods}")
# print both lists

my_foods.append("cannoli")
friend_foods.append("ice cream")
# add a different value to each list

print(f"\nMy favorite foods are:")
for food in my_foods:
    print(food)
# loop that prints everything in 'my_foods' with the addition of cannoli

print(f"\nMy friend's favorite foods are:")
for f_food in friend_foods:
    print(f_food)
# loop that prints 'friend_foods' again with the addition of ice cream
