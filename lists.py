# list - use []
# lists can have duplicates, positions (ordered) doesn't mean that it is sorted
"""
games = ["dead space", "fortnite", "elden ring", "hollow knight"]

# Slicing the list
# accessing it in the list:
# single item
print(games[-1]) # lists are zero indexed - the first element is index -1
print()
# subset of the list:
print(games[0:4:2]) #this is the same as the step function
print()
# this is the same as
print(games[::2])

# but you can crash!
# IndexError: list index out of range
#print(games[4])

#you can know how long a list is
print(len(games))
print()

# get the last element:
print(games[-1])
print(games[len(games) - 1]) # common in other languages
print()

#Looping through list elements
for game in games:
    print(game)

print()

# methods you can use for lists
print(dir(games))
games.reverse()
print(games)
games.sort(reverse=True)
print(games)

# see if an item is in the list:
print(f"is elden ring in our list: {"elden ring" in games}")
print(f"is mario in our list: {"mario" in games}")

# change an element in the list:
games[0] = "mario"
print(games)

elden_index = games.index("elden ring")
games[elden_index] = "ultrakill"
print(games)

# empty a list:
games.clear()
print(games)

# add element to the end of a list:
games.append("fortnite")
print(games)

# insert an element into a list:
games.insert(1, "donkey kong")
print(games)

# remove element from list:
games.remove("fortnite")
print(games)

# for the rest of class:
# write a program that will continuosly ask the user for their favorite thing
# take the input and add it to a list.
# when the user types Q, print the list.
"""


favorites = []
while True:
    enter = input("Enter your favorite thing: ").upper().strip()
    if enter != "Q":
        favorites.append(enter)
    elif enter == "Q":
        for i, favorite in enumerate(favorites, start = 1):
            print(f"{i}. {favorite}")
        break