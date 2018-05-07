Instructions: 
# Create a script that examines the following string for a particular letter. 
# "Python in GIS makes work easier".
# If the string does contain your letter, the script should print
# "Yes, the string contains the letter."
# If not, the script should print "No, the string does not contain the letter."


# Name: [John Marshall]
# Date: 6/20/2017
# Assignment 1 Part 1
# This script examines a string for a particular letter.
#enter code here

# first procedure:
myString = 'Python in GIS makes work easier'
print(myString)
letter = myString[1]
x = letter
print("The letter examined in the string is " + letter)
if letter == x:
    print("Yes, the string contains the letter.")
else:
    print("No, the string does not contain the letter.")

# second procedure
letters = "Geographic Information Systems"
print(letters)
x = letters.find("a")
print(x)
if x >= 0:
    print "Yes,this letter does occur in string."
if x < 0:
    print "No,this letter does not occur in string."



