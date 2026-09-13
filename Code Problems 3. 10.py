balance = int(input("What is your bank account in dollars(no $ symbol needed)?"))
if balance <= 0:
    print("Your have a negative balance and are in debt")
elif balance == 0:
    print("You have no money in your balance.")
elif 0 < balance < 99:
    print("You have a positive balance")
else: print("You be rich")
