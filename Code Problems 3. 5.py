age = int(input("How old are you?"))
if age <= 5:
    print("Your ticket costs £0.00, your entry is free!")
elif 6 <= age <= 12:
    print("Your ticket costs £5")
elif 13 <= age <= 17:
    print("Your ticket costs £8")
elif age <= 18:
    print("You are very old. Your ticket costs £10")
