myFile = open("purchases.txt","r")
total = 0
for line in myFile:
    detail = line.strip("\n")

    data = detail.split(",")
    search = "Decorating"
    if data[1] == search:
        total = total + float(data[2])
print("You have spent £" + str(total) + " on " + search + " today.")

myFile.close()
