from random import randint
guesses = 0
number = randint(0,100)
while guesses < 5:
    answer = int(input("Guess my number"))
    if answer < number:
        print("My number is higher")
    elif answer > number:
        print ("My number is lower")
    else:
        print("That's correct")
        guesses = 5
    guesses = guesses + 1
print("GAME OVER")

