'''A list index behaves like any other variable name! It can be u
sed to access as well as assign values. You saw how to access a list
index like this:

zoo_animals[0]

# Gets the value "pangolin"
You can see how assignment works on line 5:
zoo_animals[2] = "hyena"
# Changes "sloth" to "hyena"
Instructions 
Write an assignment statement that will replace the item that currently
holds the value "tiger" with another animal (as a string). It can be
any animal you like.
'''
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
 
zoo_animals[3] = "ostrich"
print zoo_animals
