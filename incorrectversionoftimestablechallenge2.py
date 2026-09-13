import random

i = 0
correct = 0
mad = 10 - i

for i in range(1,11):
    mad = 10 - i
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    answer = num1 * num2
    pupil = int(input("What is " + str(num1) + " times " + str(num2) + "? "))
    if i == 10 and answer == pupil:
        correct = correct + 1
        print("You have answered correct. You have " + str(mad) + " questions left. You got " + str(correct) + " out of 10.")
    elif i == 10 and answer != pupil:
        print("You have answered incorrect. You have " + str(mad) + " questions left. You got " + str(correct) + " out of 10.")
    elif answer == pupil:
        correct = correct + 1
        print("You have answered correct. You have " + str(mad) + " questions left.")
    else:
        print("You have answered incorrect. You have " + str(mad) + " questions left.")

