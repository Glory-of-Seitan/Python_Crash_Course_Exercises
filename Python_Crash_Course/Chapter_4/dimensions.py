dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# define tuple 'dimensions' and print both indices individually

dimensions[0] = 250
# attempt to change the value at index[0] of dimensions. This will throw an error because tuples are immutable.

my_t = (3,)
print(my_t)
# define tuple 'my_t' with 1 value and print

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
# loop that prints all values in tuple 'dimensions'

dimensions = (400, 100)
# redefine tuple 'dimensions' with new values

print("\nUpdated dimensions:")
# info message

for dimension in dimensions:
    print(dimension)
# loop that prints all values in 'dimensions'
