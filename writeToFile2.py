myFile = open("names.txt","w")

for i in range(0,5):
    name = str(input("What name? "))
    output = str(i+1) + ". " + name + "\n"
    myFile.write(output)

myFile.close()
