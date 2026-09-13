import random

guesses = 0

number = random.randint(1,100)

guess = 0

guesses = guesses + 1

while number != guess:
    if guess < number:
        print("Too low, try higher.")
    elif guess > number:
        print("Too high, try lower")
    guess = guess + 1
    guesses = guesses + 1

print("You have guessed correctly. It took you " + str(guesses) + " guesses.")

##    if guesses = 1
##        if guess > previousguess:
##            highestguess = guess
##    previousguess = guess
##    if guess 
##    guess = guess + 
