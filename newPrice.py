def newPrice(nights,room):
    if room == "basic":
        price = nights * 60
    else:
        price = nights*80
    return price
print(newPrice(5,"premium"))
