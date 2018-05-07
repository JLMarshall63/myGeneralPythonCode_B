numList = [0,1,2,3,4,5,6]
for x in numList:
    print(x)
    
x = 35
count = 0
while (count < x):
    print("The count is ", count)
    count = count + 1

print("Over and Out")

n = ["1abd","2cde","3fgh","4ijk","5lmn","6opq","7rst","8uvw"]
l = ["1","2","3"]
for m in n:
    if "a" in m:
        for k in l:
            if k in m:
                print(k)


a = 7
b = 5
c = (a**2) + (b**2)
print(c)

temp = 210

if temp > 0 and temp < 40:
    print("cool")
elif temp >=40 and temp < 75:
    print("warm")
else:
    print("HOT!")

myList = [0, 1, 3, 5, -5, -3, -1, "a", "b"]

for x in myList:
    print(x)

fruits = ['mango', 'peach', 'apple', 'orange', 'cherry']

print len(fruits)

for x in fruits:
    If x < len(fruits):
        print(x)

myList = [0, 1, 3, 5, -5, -3, -1, "a", "b"]

myList[0:6]
print(myList)