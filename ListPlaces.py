#create / print list
bikes = ['trek','redline','geowagon']
print bikes

#find first item in list
fbike = bikes[0]

#find last item in list
lbike = bikes[-1]

# print full list
print bikes

#print first item
print fbike

#print last item
print lbike

#declare variable to hold first two items
fst_two = bikes[:2]

#print first two items
print fst_two

#append a new item to list
bikes.append("Hashberry")

#print updated list
print bikes

#print reverse order updated list 
print bikes[::-1]
bikes.reverse()
print bikes
print(sorted(bikes,reverse=True))
print bikes

#sort items in list
x = [1, 3, 5, 2, 6, 4, 7]
print x
x.sort()
print "Sorted: {0}".format(x)
 
trees = ['fir','spruce','maple']
print trees
trees.sort()
print "Sorted: {0}".format(trees)

bikes = ['trek','redline','geowagon']
print bikes
bikes.sort()
print "Sorted: {0}".format(bikes)

#Count number of times items occur in a list
aList = [1, 6, 7, 45, 7, 12]
print "Count for 7: ", aList.count(7)

bList = ["weed", "native", "nonative", "weed", "ornamental", "weed"]
print "Count for weed: ", bList.count("weed")

#Insert items in a list
aList.insert(0, 7)
print aList
print "Count for 7: ", aList.count(7)

bList.insert(0, "weed")
print bList
print "Count for weed: ", bList.count("weed")

#Find the number of items in a list
num_items = len(bList)
print "There are {} items in bList".format(num_items)

#Change a list element(s)
print aList
aList[1] = 89
print aList
print bList
bList[-2] = "focal species"
print bList

#delete list element
print aList
del aList[-1]
print aList

print bList
del bList[2]
print bList

#pop last list element from list
lastItem = bList.pop()
print lastItem
print bList

#pop first list element from list
firstItem = bList.pop(0)
print firstItem
print bList

#print a list of numbers 0 to 100, 50 to 75
for n in range(101):
    print(n)

for n in range(50, 76):
    print(n)    

#find the min, max, total

ages = [35, 65, 65, 23, 72, 23, 54, 41]
print ages

youngest = min(ages)
print youngest

oldest = max(ages)
print oldest

total = sum(ages)
print total

# avg in list

avg = sum(ages)/ float(len(ages))
print avg

#Slicing a list first three, middle two, and last two and

myLista = ["eeny", "miney", "moe", "one", "big", "toe", "corn"]
first_three = myLista[:3]
print first_three
middle_three = myLista[2:5]
print middle_three
last_three = myLista[-3:]
print last_three

#convert to upper/lower case
myListb = ["dopey", "sleepy", "grumpy", "trippy", "lippy", "whacky", "sappy"]

upper_case = []
for x in myListb:
    upper_case.append(x.upper())
print upper_case

lower_case = []
for x in myListb:
    lower_case.append(x.lower())
print lower_case

