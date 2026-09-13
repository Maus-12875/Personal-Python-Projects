def timesTable(number):
    for i in range(1,13):
        new = number * i
        print(str(i) + " x " + str(number) + " = " + str(new))

number = int(input("What number would you like? "))

timesTable(number)
