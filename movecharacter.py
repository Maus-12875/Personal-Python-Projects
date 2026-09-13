def moveCharacter(position,direction):
    if direction == "right":
        position = position + 5
        if position > 512:
            position = 512
    else:
        position = position - 5
        if position < 1:
            position = 1
    return position
    
import random

position = random.randint(1,512)

print("The position is " + str(position))
direction = ""
while direction != "left" and direction != "right":
    direction = input("Enter direction, left or right")
    print(moveCharacter(position,direction))
