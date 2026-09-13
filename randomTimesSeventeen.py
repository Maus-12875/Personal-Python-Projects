import random

def newNumber(random):
    multiplied = random * 17
    textfile = open("numberStore","w")
    textfile.write(str(multiplied))
    textfile.close()

random = random.randint(1,10)
newNumber(random)
