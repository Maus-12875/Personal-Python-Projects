numbers = [5,2,99,18,45,66,17,1,8,15,3,28,107]
searchValue = 107
found = False
end = False

while found == False and end == False:
    for i in range(0,len(numbers)):
        if numbers[i] == searchValue:
            found = True
        else:
            print("Number " + str(searchValue) + " not found.")            
    if found == True:
        print("Number " + str(searchValue) + " found at " + str(numbers[i]) + ".")
    elif end == False and found == False:
        end = True
        print("Number " + str(searchValue) + " not found in list.")
        
