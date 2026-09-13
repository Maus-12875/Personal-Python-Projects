#Exercise 1: Variable and Constant Practice
player_score = 0
MAX_ROLLS = 3
print(player_score)
print(MAX_ROLLS)

#Exercise 2: Understanding Assignment and Operators
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum is:", sum)

#Exercise 3: Fix the Bug - Input and Casting

#Exercise 4: Debugging and Output Formatting

#Exercise 5: The Beat that Dice Game (Challenge Task)
import random
highscore = 0
total = 0
stop = "y"

while stop != "n":
    roll = input("Enter i to roll the dice.").lower()
    if roll == 'i':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        rolltot = str(die1) + str(die2)
        total = total + int(rolltot)
        print(str(die1))
        print(str(die2))
        if die1 > die2:
            print(str(die1) + str(die2))
        if int(rolltot) > int(highscore):
            highscore = rolltot
            print("New highscore is " + str(highscore) + ".")
            stop = input("Do you want to re-roll? ").lower()
        elif die2 > die1:
            print(str(die1) + str(die2))
            stop = input("Do you want to re-roll? ").lower()
        else:
            print("You rolled a double. Re-roll!")

print(str(highscore))

#Extra task
flag = False

while flag == False:
    num = input("Enter something: ")
    if num.isdigit() == True:
        flag = True
