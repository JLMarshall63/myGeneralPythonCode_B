inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    
}
print inventory
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here

#add pocket key and values
inventory['pocket'] = ["seashell","strangeberry", "lint"]

# for inventory dictionary display added key and it values
print inventory

#sort contents of backpack key in inventory dictionary
inventory['backpack'].sort()
#from inventory dictionary reove dagger value from backpack key
inventory['backpack'].remove("dagger")
#add 40 to the value in the gold key
inventory['gold'] += 50

# for inventory dictionary display key (backpack) with its values (dagger) removed
print inventory
