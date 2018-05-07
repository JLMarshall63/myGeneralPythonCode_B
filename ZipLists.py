x = [1, 2, 3, 4]

y = [7, 4, 2, 1]

z = ["a", "b", "c", "d"]

u = zip(x, y, z)

print u

for a, b, c in zip(x,y, z):
    print (a, b, c)

print(zip(x,y,z))

print (list(zip(x,y,z)))
print (dict(zip(y,z)))

for i in zip(x, y, z):
    print i

#[print(a,b,c) for a,b,c in zip(x,y,z)]

#print (x,y) for x,y in zip(x,y)    