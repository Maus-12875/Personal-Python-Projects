grades = [2,3,4,5,6,7,8]
found = False
left = 0
right = len(grades) - 1
while found == False and left <= right:
    mid = (left + right)//2
    if grades[mid] == 7:
        found = True
    else:
        if 7 > grades[mid]:
            left = mid + 1
        else:
            right = mid - 1
print("Number seven found at position " + str(mid) + ".")
