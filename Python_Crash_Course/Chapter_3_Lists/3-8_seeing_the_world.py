places = ["Tivoli", "Berlin", "Ethiopia", "Iceland", "Thailand"]
print("\nHere's some places I'd love to travel:", places)
# create list 'places' and print

print("\nHere they are alphabetized:", sorted(places))
# sort 'places' and print in alphabetical order

print("\nBut they don't need to be alphabetized:", places)
# print 'places again to show that it isn't permanently altered

print(
    "\nThey can be in reverse alphabatized order if we want to be fancy:",
    sorted(places, reverse=True),
)
# temp sort places to be in reverse alphabetical order and print

print("\nThe list is still intact since we've only used 'sorted()':", places)
# prove list hasn't been altered

places.reverse()
print("\nNow let's reverse the list for real:", places)
# reverse the list and print it

places.reverse()
print("\nAnd back to how it started:", places)
# revrse the list again so it's back to normal and print

places.sort()
print("\nAnd now it's alphabetical for good with 'sort':", places)
# sort into alphabetical permanently with sort() and print

places.sort(reverse=True)
print("\nBut sorting goes both ways if 'reverse=True':", places, "\n")
# sort() in reverse and print
