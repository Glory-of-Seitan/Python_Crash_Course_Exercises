sando_orders = [
    "grilled cheese",
    "tofurky",
    "spinach",
    "reuben",
    "pb & j",
]

finished_sandos = []


while sando_orders:
    current_sando = sando_orders.pop()

    print(f"I made your {current_sando} sandwich.")
    finished_sandos.append(current_sando)

print("\nThe following sandwiches were made for lunch:")
for sando in finished_sandos:
    print(sando.title())
