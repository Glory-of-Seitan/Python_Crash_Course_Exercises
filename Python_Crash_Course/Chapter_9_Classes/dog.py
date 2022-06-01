#create a class named 'Dog' that can define individual dogs
class Dog:
    """A simple attempt to model a dog."""

    #__init__ is used to initialize the class (still don't quite 
    # understand)
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    #define a function within the class called 'sit()'. 
    #this can be called as a method with the '.' notation
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    #define the method 'roll_over'
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


### Creating Instances ###

my_dog = Dog('Muffin', 14)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

### Creating Multiple Instances ###

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
