prompt = "\nPlease enter the name of a city you've visited."
prompt += "\nEnter 'quit' to end the program\n: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()} this time of year.")