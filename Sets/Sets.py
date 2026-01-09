#Sets
#A set is a collection which is unordered, unchangeable*, and unindexed.
#* Note: Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
print("Welcome to set module")
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("Type of thisset:",   type(thisset))
print("Length of the set:",len(thisset))  #Finding the length of the set

#Sets cannot have duplicate items.
#Duplicate items will be ignored
thisset = {"apple", "banana", "cherry", "apple", "banana"}
print("Set after adding duplicate items:",thisset)

#Sets are unordered, so the items will appear in a random order
#Set items can be of different data types
#1 and true are treated as the same value in sets, false is also treated as the same value.
print("Set with mixed data types:", {1, "Hello", 3.4, True}) 

thisset.add("orange")  #Adding an item to the set       
print("Set after adding an item:",thisset)
thisset.update(["mango", "grape"])  #Adding multiple items to the set   
print("Set after adding multiple items:",thisset)
thisset.remove("banana")  #Removing an item from the set, raises an error if the item to remove does not exist
print("Set after removing an item:",thisset)
thisset.discard("cherry")  #Removing an item from the set, does not raise an error if the item to remove does not exist
print("Set after discarding an item:",thisset)
thisset.pop()  #Removes a random item from the set
print("Set after popping an item:",thisset) 
#del keyword  #Deletes the set completely

#cant access items in a set by index because sets are unordered
#loop through the set items
for item in thisset:
    print("Set item:",item)
#Check if an item is in the set
print("Is 'apple' in the set?", "apple" in thisset)


#union of sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("Union of set1 and set2:",set3)
#intersection of sets
set4 = {"a", "b", "c", 1, 2, 3}
set5 = {"a", "b", 4, 5, 6}
set6 = set4.intersection(set5)
print("Intersection of set4 and set5:",set6)
#symmetric difference of sets
set7 = set4.symmetric_difference(set5)
print("Symmetric difference of set4 and set5:",set7)
# | operator for union
set8 = set1 | set2
print("Union using | operator:",set8)
