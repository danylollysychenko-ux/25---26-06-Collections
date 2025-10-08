"""
Sets are also collections
They are not ordered - meaning they don't have a fixed position - can't access by index
You CANNOT change existing items, but you can add/remove them
Advantage: DOES NOT ALLOW DUPLICATES
"""

# notice sets us curly braces { }
trees = {"evergreen", "maple", "hickory", "oak"}
print(trees) # prints in a random order
# you cannot access elements by index - because it's unordered
#print(trees[0]) # CRASH - TypeError: "set" object is not subscriptable

# add and remove from list
trees.add("palm") # note: this is ADD not append (that lists use)
print(trees)
trees.remove("evergreen")
print(trees)
# sets do not allow duplicates
trees.add("palm")
print(trees) # palm was not added a second time

# quick trick to get clean lists - if order doesn't matter.
my_list = ["Bennet", "Bennet", "Bennet", "Draven", "Levi", "Liam"]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)