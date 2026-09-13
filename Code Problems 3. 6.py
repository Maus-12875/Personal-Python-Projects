temprature = int(input("What is the temprature (please input the temp in Celcius, without the symbol)?"))

if temprature > 30:
    print("The temprature is hot!")
elif 20 <= temprature <= 30:
    print("The temprature is warn")
else: print("The temprature is cold. Brr!")
