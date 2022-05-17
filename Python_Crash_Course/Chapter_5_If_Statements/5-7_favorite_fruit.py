fav_fruits = ["banana", "mango", "orange"]
fruit_asks = ["banana", "lime", "dragonfruit", "orange", "mango", "lemon"]
fruit = "x"
fruit_liked = f"It is true, I have great love for "
fruit_no_bueno = f"No thanks, those are gross"
print("")

for fruit in fruit_asks:
    if fruit in fav_fruits:
        print(f"{fruit_liked}{fruit}s.\n")
    if fruit not in fav_fruits:
        print(f"{fruit.title()}s? {fruit_no_bueno}.\n")
