# Name: John Marshall
# Date: 6/22/2017
# Description: This script demonstrates how to break a loop
from math import sqrt
for i in range(1001, 0, -1):
    root = sqrt(i)
    if root == int(root):   #This evaluates whether the root is an integer
        print i
        break