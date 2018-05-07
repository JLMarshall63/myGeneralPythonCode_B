'''
Maintaining Order

Sometimes you need to search for an item in a list.

animals = ["ant", "bat", "cat"]

print animals.index("bat")

First, we create a list called animals with three strings.
Then, we print the first index that contains the string "bat",
which will print 1.

We can also insert items into a list.
animals.insert(1, "dog")

print animals

We insert "dog" at index 1, which moves everything down by 1.

We print out ["ant", "dog", "bat", "cat"]

'''
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]


# Your code here!

print animals.index("duck")

duck_index = animals.index("duck") # Use index() to find "duck"

animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation


