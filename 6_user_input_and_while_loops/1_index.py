# User input
# message = input("Type something here as an input")

# print(f"The message is {message}")

# While loops
age = 15

while age > 1:
    
    if age < 17:
        print(f"This is age: {age} is still under age")
    
    if age >= 18:
        print(f"This age: {age} is now a legal age")
        break
        
    age += 1