# Tuples - just like list but they cannot change
# items cannot be added, removed, or have a new position
# values that cannot change are called "immutable"

# Tuple with one item only
tupleSample = ("one,")

# You can update a tuple by making it into a list temporarily and create it again as a tuple
# this is same with other CRUD functionalities
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Unpacking a tuple
# same concept on deconstructuring in javascript, but in here you can rename the variable
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Asterisk in tuple
# this means that the rest of items will be the same as the variable with the *
fruits = ("apple", "banana", "cherry")
(green, yellow, *red) = fruits

""" output:
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

