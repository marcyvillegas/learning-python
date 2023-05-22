# Passing an arbitary number of arguments
# - passing any number and type of arguments

# What is *args
# *args - allows us to pass a variable number of non-keyword arguments to a function
# Non-keyword here means that the arguments should not be a dictionary (key-value pair), and they can be numbers or strings
def multiplyNumbers(*numbers):
    product=1
    for n in numbers:
        product*=n
    return product
 
print("product:",multiplyNumbers(4,4,4,4,4,4)) 

# What is **kwargs
# **kwargs - allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
def makeSentence(**words):
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence
 
print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))

# -- Modules -- 
import module as musicMaker

musicMaker.createMusic("piano", "guitar")