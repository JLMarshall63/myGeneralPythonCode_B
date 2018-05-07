# Directions: Complete the functions below. The first one is done for you. The tests at the bottom
#should run and print out values you'd expect. 

# Geog 565 2016 Assignment 6 Part 1
# Name: John Marshall
# Date: 7/25/2017
# This script creates and test 3 functions

# the triangle fucntion takes in 3 numbers and returns the type of triangle
def triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif (a != b and a != c and b != c):
        return "none"
    else:
        return "isosceles"

# the absolutevalue function takes in an integer and returns the absolute value of that integer
# you can assume there will only be integers as input
# the absolute value of a number is always positive
# for example: the absolute value of 5 is 5; the absolute value of -5 is 5

def absolutevalue(num):
    # your code here
    x = abs(num)
    return x
# the absolutevalues function takes in a list of integers and returns a list of the absolute values
#of the original list this is similar to the absolutevalue function except you need to loop through
#the input list and return a list.append

list = []

def absolutevalues(numlist):
    for x in numlist:
        list.append(abs(x))
    return list
  
# Tests - do not remove. These will help you know your functions are working. Feel free to add more!
# triangle tests

print "Triangle Tests: "

print triangle(2,2,2)
print triangle(2,2,5)
print triangle(1,2,3)

# absolutevalue tests

print "Absolute Value Tests: "

print absolutevalue(-5)
print absolutevalue(10)

# absolutevalues tests

print "Absolute Values Tests: "

print absolutevalues([1,2,-2,-5])
print absolutevalues([-11,-12,2,-5])
print absolutevalues([-67,-99,10,123])  
