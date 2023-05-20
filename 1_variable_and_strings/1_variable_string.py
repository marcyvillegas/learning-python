# hello world
# print("Hello World")

# variable
message = "hello python"
print(message)

# --- VARIABLE ---

# Multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# --- STRINGS ---
# more on https://www.w3schools.com/python/python_strings.asp 

# this data type has also built-in methods like:
name = "marcy"
nameLowerCase = name.lower()

# Using variables as string
introduce = f"Hello my name is {name.title()}"
print(introduce)

# Strings are arrays
a = "This is an array"
print(a[0])

# You can loop through a string since it is an array
def loopString():
    for x in "sample":
        print(x)


loopString()  # calling the function]