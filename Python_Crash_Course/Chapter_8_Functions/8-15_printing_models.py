from printing_functions import print_models, show_completed_models


# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

#run the two functions on the list of designs
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
