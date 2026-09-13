names = []

for i in range(10):
    name = input("Enter a name: ")
    names.append(name)
    
for i in range(10):
    print(str(i +1) + ". " + names[i])
