n = [1, 3, 5]
print n
print n[1] * 5
# Add your code below
print n[1]
print n[1] * 5

# Do your multiplication here
x = n[1] * 5
n[1] = x
print n
p = 4
u = [4]
n.append(p)
n.append(u)
print n

n.pop(0)
print n

n.remove([4])
print n

del(n[1])
print n