from random import randint


class Die:
    """A class that attempts to model dice and their rolls"""

    def __init__(self, sides):
        """Initializes one or more dice (number) with X sides (sides)"""
        self.sides = sides

    def roll_die(self, number=1):
        """Rolls (number) of (self) dice"""
        for roll in range(0, number):
            print(randint(1, self.sides))


print(f"\nRolling 10 d6's:")
d6 = Die(6)
d6.roll_die(10)

print(f"\nRolling 10 d10's:")
d10 = Die(10)
d10.roll_die(10)

print(f"\nRolling 10 d20's:")
d20 = Die(20)
d20.roll_die(10)
