x = []

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!

#Create a function that returns the sum of a list of numbers

numbers = [3, 5, 7]
def total(numbers):
    for i in range(0, len(numbers)):
        numbers[i]
    y = sum(numbers)
    return y

n = [3, 5, 7, 10]
print total(n)

words = []

# Add your function here
def join_strings(words):
    y = ''.join(words)
    return y
 
n = ["Michael", "Lieberman"]
print join_strings(n)

words = []

# Add your function here
def join_strings(words):
    y = ''.join(words)
    return y
 
n = ["Michael"," ", "Lieberman"," ","McDonald"]
print join_strings(n)