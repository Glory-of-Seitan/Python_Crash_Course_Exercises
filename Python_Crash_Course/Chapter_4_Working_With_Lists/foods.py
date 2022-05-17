my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
# create a (disturbingly accurate) list of favorite foods for me and a friend. The friend's list is a slice containing everything in my list

print(f"My favorite foods are:\n{my_foods}")
print(f"My friend's favorite foods are:\n{friend_foods}")
# print both lists

my_foods.append("cannoli")
friend_foods.append("ice cream")
# add a different value to each list

print(f"My favorite foods are:\n{my_foods}")
print(f"My friend's favorite foods are:\n{friend_foods}")
# print both lists again to prove they are different
