"""
A tuple is:
Ordered (we access elements by index)
Unchangeable (immutable) - we cannot add/remove or change values
Allows duplicates
Faster than a list
""" 

# tuples use ()
fruits = ("apple", "banana", "orange", "tomato", "apple")
print(fruits)
print(len(fruits))
print(fruits[1])

# see if value in tuple:
print("apple" in fruits)
print("dragon fruit" in fruits)

# count items in fruits
print(fruits.count("apple")) #2

# find index of element:
print(fruits.index("banana")) #1
#print(fruits.index("car")) # Throws ValueError - if element is not in the tuple

# Loop through a tuple:
for fruit in fruits:
    print(fruit)

print("-------------------------------")

# while loop through tuple
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
    if index == len(fruits):
        break