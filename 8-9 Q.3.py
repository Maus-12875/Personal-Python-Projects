def calcVolume(itemWidth, itemHeight, itemLength):
    volume = itemWidth * itemHeight * itemLength
    return volume

itemWidth = int(input("Enter width "))
itemHeight = int(input("Enter height "))
itemLength = int(input("Enter length "))
itemVolume = calcVolume(itemWidth, itemHeight, itemLength)
if itemVolume > 1000:
    print("error")
else:
    print("Volume is " + str(itemVolume))
