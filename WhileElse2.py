from random import randint

# Generates a number from 1 through 10 inclusive
#random_number = randint(1, 11)

print "You have 3 chances to guess a luckynumber. If the numbers do not match, you lose.!"

guesses_left = 3
while (guesses_left > 0 and  guesses_left <= 3):
    random_number = randint(1, 11)
    guess = int(raw_input("Enter your lucky number guess here!"))
    print guess
    print random_number
    if guess != random_number:
        print "Sorry, you lose!"
        guesses_left -= 1
#break  
else:
    print "You win!"