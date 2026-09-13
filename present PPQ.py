studentnames = ['Rob', 'Anna', 'Huw', 'Emma', 'Patrice', 'Iqbal']
pcount = 0
absent = 0

for i in range(0, len(studentnames)):

    present = str(input("Is " + studentnames[i] + " present? ")).upper()

    if present == "Y":
        pcount = pcount + 1
        
    else:
        absent = absent + 1

print("There are " + str(pcount) + " students present")
print("and " + str(absent) + " students absent")
