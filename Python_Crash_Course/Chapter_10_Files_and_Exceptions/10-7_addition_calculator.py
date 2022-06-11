while True:
    print("\nEnter 'q' to quit.")
    print("Enter two numbers and I will add them together.")
    try:
        num_a = input("First number: ")
        if num_a.lower() == "q":
            break
        num_a = int(num_a)

        num_b = input("Second number: ")
        if num_b.lower() == "q":
            break
        num_b = int(num_b)
    except ValueError:
        print("One or both of the numbers you entered was, in fact, not a number :(")
    else:
        answer = num_a + num_b
        print(f"Answer = {answer}")
