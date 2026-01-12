#Dictionary are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)
print("Welcome to dictionary module")
print("Type of thisdict:",type(thisdict))
print("Length of the dictionary:",len(thisdict))  #Finding the length of the dictionary

#Accessing items in the dictionary by key
print("Value of 'brand' key:",thisdict["brand"])
print("Value of 'model' key using get():",thisdict.get("model"))

#Changing values in the dictionary
thisdict["year"]=2020
print("Dictionary after changing the 'year' value:",thisdict)

#Adding items to the dictionary
thisdict["color"]="red"
print("Dictionary after adding a new key:value pair:",thisdict)

#Add multiple items to the dictionary using update() method
thisdict.update({"price":30000,"mileage":15000})
print("Dictionary after updating with multiple key:value pairs:",thisdict)

#Removing items from the dictionary
thisdict.pop("model")  #removes item with specified key
print("Dictionary after popping the 'model' key:",thisdict)
thisdict.popitem()  #removes the last inserted item
print("Dictionary after popping the last item:",thisdict)
del thisdict["brand"]  #removes item with specified key
print("Dictionary after deleting the 'brand' key:",thisdict)
#thisdict.clear()  #empties the dictionary
#print("Dictionary after clearing all items:",thisdict)
#Looping through the dictionary keys

for key in thisdict:
    print("Dictionary key:",key)
#Looping through the dictionary values
for value in thisdict.values():
    print("Dictionary value:",value)
#Looping through both keys and values
for key, value in thisdict.items():
    print("Dictionary key:value pair:",key,":",value)
#Copying a dictionary
dictcopy=thisdict.copy()
print("Copied dictionary:",dictcopy)
#Using dict() constructor to make a dictionary
newdict=dict(name="John", age=30, city="New York")
print("New dictionary using dict() constructor:",newdict)
print("Type of newdict:",type(newdict))
#Nested dictionary
nesteddict={
    "person1":{"name":"Alice","age":25},
    "person2":{"name":"Bob","age":30}
}
print("Nested dictionary:",nesteddict)
print("Accessing nested dictionary item (person1's name):",nesteddict["person1"]["name"])

#Dictionary methods
print("Dictionary keys:",thisdict.keys())
print("Dictionary values:",thisdict.values())
print("Dictionary items:",thisdict.items())
print("Welcome to dictionary module end")