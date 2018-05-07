import random
x = random.randint(0, 10)
print x
if x == 6:
    print "You win!"
elif x == 5:
    print "Try again!"
else:
    print "You lose!"