##def insertionsort(names):
##
##
##    for i in range(1, len(names)):
##        pos = i
##        
##        while (pos > 0 and names[pos] < names[pos - 1]):
##            temp = names[pos]
##            names[pos] = names[pos - 1]
##            names[pos - 1] = temp
##            pos = pos - 1
##    return names
##
##names = ["Gabriel", "Johnny", "Hadrian", "Sani", "David", "Lowell", "Nicholas", "Yumn", "Hezekiah", "Gabby", "Xar", "Marcus", "Arthur", "Lucas"]
##
##print(insertionsort(names))
##
##def insertionsort(names):
##
##
##    for i in range(1, len(names)):
##        pos = i
##        
##        while (pos > 0 and names[pos] < names[pos - 1]):
##            temp = names[pos]
##            names[pos] = names[pos - 1]
##            names[pos - 1] = temp
##            pos = pos - 1
##        print(names)
##
##names = ["Gabriel", "Johnny", "Hadrian", "Sani", "David", "Lowell", "Nicholas", "Yumn", "Hezekiah", "Gabby", "Xar", "Marcus", "Arthur", "Lucas"]
##
##insertionsort(names)

##names = ["Gabriel", "Johnny", "Hadrian", "Sani", "David", "Lowell", "Nicholas", "Yumn", "Hezekiah", "Gabby", "Xar", "Marcus", "Arthur", "Lucas"]
##
##swaps = True
##
##while swaps == True:
##    swaps = False
##    for i in range(0, len(names)-1):
##        if names[i] > names[i + 1]:
##            temp = names[i]
##            names[i] = names[i + 1]
##            names[i+1] = temp
##            swaps = True
##
##print(names)
##
##names = ["Gabriel", "Johnny", "Hadrian", "Sani", "David", "Lowell", "Nicholas", "Yumn", "Hezekiah", "Gabby", "Xar", "Marcus", "Arthur", "Lucas"]
##
##def bubblesort(names): 
##    swaps = True
##
##    while swaps == True:
##        swaps = False
##        for i in range(0, len(names)-1):
##            if names[i] > names[i + 1]:
##                temp = names[i]
##                names[i] = names[i + 1]
##                names[i+1] = temp
##                swaps = True
##    return(names)
##
##print(names)

names = ["Gabriel", "Johnny", "Hadrian", "Sani", "David", "Lowell", "Nicholas", "Yumn", "Hezekiah", "Gabby", "Xar", "Marcus", "Arthur", "Lucas"]

def binarysearch(names, search):
    found = False
    first = 0
    last = len(names)-1
    while first <= last and found == False:
        midpoint = (first + last)// 2
        if names[midpoint] == search:
            found = True
        else:
            if names[midpoint] < search:
                first = midpoint + 1
            else:
                last = midpoint -1
    if found == True:
        return ("Item found at position ", + str(midpoint))
    else:
        return ("Item not found ")
search = "Johnny"
print(names)
