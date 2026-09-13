pin = input("Enter your PIN. ")

length = len(pin)
if length == 4:
    if pin == "1234" or pin == "4321":
        print("INVALID PIN")
    else:
        print("VALID PIN")
else:
    print("INVALID PIN")
