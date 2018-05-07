n = [3, 5, 7]

for i in range(0, len(n)):
    print n[i]
x = []

def print_list(x):
    for i in range(0, len(x)):
        print x[i]
        
z = [5, 7, 8, 3, 2]
print_list(z)

x = []

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
        print x[i]
        
# Don't forget to return your new list!

n = [1, 2, 3, 4, 5]
double_list(n)

x = []

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
        
# Don't forget to return your new list!

n = [1, 2, 3, 4, 5]
print double_list(n)
        
        