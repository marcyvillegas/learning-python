legalAge = 18
underAge = 17

def checkAge(age):
    if age <= legalAge:
        return "This is a legal age"
        
    return f"This is under age. The age can be {underAge} or below"

print(checkAge(22))
print(checkAge(10))

# -- TERNARY OPERATORS / CONDITIONAL EXPERSSIONS --
a = 200
b = 33
c = 500

# AND
if a > b and c > a:
  print("Both conditions are True")

# OR
if a > b or a > c:
  print("At least one of the conditions is True")
  
# NOT
if not a > b:
  print("a is NOT greater than b")
  
# -- PASS STATEMENT --
# if statement with no content, put in the pass statement to avoid getting an error
if b > a:
  pass
