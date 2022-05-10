# define the prompt that will appear before the user is asked for input
prompt = "\nTell me something and I'll repeat it."
prompt += "\nEnter 'quit' to end the program: "

# define the variable 'message' so the while loop has something to check
message = ""
# this while loop will run and ask for user input over and over
# until 'quit' is entered. Everything else will be parroted back at
# the user. With 1 exception
while message != "quit":
    message = input(prompt)
    if message.lower() == "i'm an idiot":
        print("You're an idiot")
    # this block prevents the program from printing 'quit' before
    # closing the program
    elif message != "quit":
        print(message)
