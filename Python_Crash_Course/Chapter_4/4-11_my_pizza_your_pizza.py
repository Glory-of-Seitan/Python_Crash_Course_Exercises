pizzas = ["bbq chik'n", "pineapple", "taco"]
# make list 'pizzas'

friend_pizzas = pizzas[:]
# copy list 'pizzas

pizzas.append("sausage ranch")
friend_pizzas.append("pepperoni with other stuff")

print("\n")
# print 2 blank lines

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
# loop that prints the items on 'pizzas' after a message

print("\nMy friend's favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza, "")
# loop that prints the items on 'friend_pizzas' after a message

print("")
# print blank line at the end
