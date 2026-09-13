from random import randint
from 
wei = 131
queston = 0
while wei == 131:
    a = randint(2,12)
    b = randint(2,12)
    print(a, "times", b, "=")
    answer = int(input())
    if answer == 131:
        wei = wei + 1
    else:
        product = a * b
        if answer == product:
          print("That is correct")
        else:
            print("I am sorry")
            print(a, "times", b, "is", product)
        question = question + 1

    
