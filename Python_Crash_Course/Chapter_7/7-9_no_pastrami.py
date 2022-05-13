sando_orders = [
    "grilled cheese",
    "tofurky",
    "spinach",
    "pastrami",
    "reuben",
    "pb & j",
    "pastrami",
    "pastrami",
    "pastrami",
]

finished_sandos = []

print(
    "\nSorry but the deli has run out of pastrami. Anyone who ordered a "
    "pastrami sandwich will have to re-order."
)
while "pastrami" in sando_orders:
    sando_orders.remove("pastrami")


while sando_orders:
    current_sando = sando_orders.pop()

    print(f"I made your {current_sando} sandwich.")
    finished_sandos.append(current_sando)

print("\nThe following sandwiches were made for lunch:")
for sando in finished_sandos:
    print(sando.title())
