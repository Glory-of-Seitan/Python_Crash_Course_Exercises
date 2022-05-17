animals_that_could_be_an_even_fight_for_a_human = [
    "eagle",
    "goat",
    "boa constrictor",
    "dog",
    "chimpanzee",
    "deer",
    "goose",
    "baboon",
    "bobcat",
]
# define list of animals that could go toe to toe with a human without being a sure bet

print("\n", animals_that_could_be_an_even_fight_for_a_human)
# print said list

print("\n", sorted(animals_that_could_be_an_even_fight_for_a_human))
# print the list alphabetically for no reason

answers = []
# define an empty list for the user's answers before the loop


for times in range(len(animals_that_could_be_an_even_fight_for_a_human)):
    # begin loop to ask if user could fight each animal

    q_animal = animals_that_could_be_an_even_fight_for_a_human.pop(0)
    # pop the first animal on the list as 'q_animal'

    print("\nDo you think you could win in a fight vs a", q_animal, "?\nY/N:")
    # ask if user thinks they will win the fight against 'q_animal'

    answer = input()
    # user input recorded as 'answer'

    animals_that_could_be_an_even_fight_for_a_human.append(q_animal)
    # append q_animal onto the original list to leave it reconstructed in the same order after a full pass through

    answers.append(answer)
# append the user answer into the list 'answers'

# end first loop, begin second

print("")
# print a new line

for times in range(len(animals_that_could_be_an_even_fight_for_a_human)):
    print(animals_that_could_be_an_even_fight_for_a_human.pop(0), "=", answers.pop(0))
# run a loop that prints each animal connected to its answer and empties the lists with pop()

print(animals_that_could_be_an_even_fight_for_a_human)
print(answers)
# print both empty lists


# A simpler way of doing it is below:

#  for animal in animals_that_could_be_an_even_fight_for_a_human:
#  print("\nDo you think you could win in a fight vs a ",animal,"?\nY/N:")
#  answer = input()
#  answers.append(answer)

# Only the lens() and sorted() functions were introduced in this chapter. All others were methods and statements
