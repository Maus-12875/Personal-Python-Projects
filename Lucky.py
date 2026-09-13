from random import randint
lucky = randint(1,100)
guessed = False
noguesses = 0
lives = 3
while guessed == False and lives >= 1:
    print("Can you guess my lucky number? You have", lives, "guesses.")
    if noguesses == 0:
        print("It is between 1 and 100.")
    guess = int(input())
    if guess != lucky:
        print("Sorry, it's not", guess, ".")
        if guess >= lucky:
            print("My lucky number is less than", guess, ".")
        else:
            print("My lucky number is more than", guess, ".")
        noguesses = noguesses + 1
        lives = lives - 1
    else:
        print("Amazing, you guessed it. It took you", noguesses, "guesses.")
        guessed = True
if guessed == True:
    print("Nice playing with you")
else:
    print("Sorry, my lucky number is ", lucky, ". GAME OVER")
