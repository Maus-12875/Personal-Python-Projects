time = int(input("What is the time in hours (eg. 19, or 5)?"))
if time == 3:
    print("Error")
elif 4 <= time <= 12:
    print("Good morning.")
elif 13 <= time <= 15:
    print("Good afternoon.")
elif 17 <= time <= 20:
    print("Good evening.")
elif 21 <= time <= 24:
    print("Go to sleep.")
elif 0 <= time <= 2:
    print("Go to sleep. Or wake up. It's too hard to tell which.")
