""" 
Python Collections (Arrays)
There are four collection data types in the Python programming language:

= List is a collection which is ordered and changeable. Allows duplicate members.
= Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
= Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
= Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# -- LISTS --- 
# List - collection of items in a particular order
# - this is also pretty similar to arrays

# Accessing items on the list
sampleList = ["first", "second", "third"]
print(sampleList[0:2]) # first param: what position it will start, second param: up to what number

# Negative index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # starts from the last and does not include the index

# you can do CRUD functionalities, sort, join, loop, copy
# more on https://www.w3schools.com/python/python_lists_change.asp 

# --- List Comprehension ---
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# turn ^ into:
newlist = [x for x in fruits if "a" in x]

print(newlist)

# newlist = [expression for item in iterable if condition == True]