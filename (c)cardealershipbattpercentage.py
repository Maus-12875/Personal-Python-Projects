charge = int(input("What is the current battery charge percentage? "))

if charge == 100:
    print("full")
elif charge < 100:
    remainingcharge = 100 - charge
    time = remainingcharge*10
    hours = time // 60
    minutes = time % 60
    print("You have " + str(hours) + " hours and " + str(minutes) + " left.")
