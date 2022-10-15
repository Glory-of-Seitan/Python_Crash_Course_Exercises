print("")
print("Enter two numbers and I will add them together.")
try:
    num_a = int(input("First number: "))
    num_b = int(input("Second number: "))
except ValueError:
    print("One or both of the numbers you entered was, in fact, not a number :(")
else:
    answer = num_a + num_b
    print(f"Answer = {answer}")
