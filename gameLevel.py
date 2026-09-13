code = "0"
level = 0

while len(code) != 3:
    code = input("Enter the level code. ")
    if code.upper() == "SVA":
        level = 2
    elif code.upper() == "UTV":
        level = 3
    else:
        level = 1
print(level)

def nextlevel(level):
    if level != 3:
        level = level + 1
    elif level == 3:
        level = 1
    return(level)

print(nextlevel(level))

nextlevel = nextlevel(level)

textfile = open("levels.txt","a")

textfile.write(str(nextlevel))

textfile.close()
