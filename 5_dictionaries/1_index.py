# Dictionaries - are like objects in javascript
# they store "key": "value" pairs
# duplicating of keys are not allowed

# Accessing the items
user = {
    "name": "Marcy",
    "age": 12,
    "hobbies": ["music", "programming"]
}

name = user["name"]
age = user.get("age")
allKeys = user.keys()
allValues = user.values()
allItems = user.items()


