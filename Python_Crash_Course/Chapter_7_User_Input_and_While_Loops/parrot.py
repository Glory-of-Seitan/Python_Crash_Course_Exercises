# define the prompt that will appear before the user is asked for input
prompt = "\nTell me something and I'll repeat it."
prompt += "\nEnter 'quit' to end the program: "

active = True

# define the variable 'message' so the while loop has something to check
message = ""
# this while loop will run and ask for user input over and over
# until 'quit' is entered. Everything else will be parroted back at
# the user. With 1 exception
while active == True:
    message = input(prompt)
    if message == "quit":
        active = False
    elif message.lower() == "i'm an idiot":
        print("You're an idiot")
    # this block prevents the program from printing 'quit' before
    # closing the program
    else:
        print(message)
