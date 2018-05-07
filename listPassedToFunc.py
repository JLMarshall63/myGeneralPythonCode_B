def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

def first_item(items):
    print items[0]

numbers = [2, 7, 9]
print list_function(n)
first_item(n)
first_item(numbers)

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

def list_function(x):
    z = x[1] + 3
    x[1] = z
    return x

n = [3, 5, 7]
print list_function(n)

n = [3, 5, 7]
print n
# Add your function here
def list_extender(n):
    x_list = [9]
    x_list.append(n)
    return x_list
    
print list_extender(n)

n = [3, 5, 7]
#print n
# Add your function here
def list_extender(n):
    x = 9
    n.append(x)
    return n
    
print list_extender(n)
