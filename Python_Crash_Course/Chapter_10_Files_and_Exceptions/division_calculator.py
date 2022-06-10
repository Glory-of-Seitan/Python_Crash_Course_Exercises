### USING EXCEPTIONS TO PREVENT CRASHES ###

print(
    f"Give me two numbers. ANY two numbers. And I will tell you how the root "
    f"of those numbers, is Greek."
)
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
            print("One cannot simply divide by zero.")
    else:
        print(answer)

