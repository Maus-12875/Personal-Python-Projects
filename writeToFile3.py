myFile = open("pilots.txt","a")

code = str(input("What is your pilot code? "))
dob = str(input("What is your date of birth? "))
output = str(code) + "," + str(dob) + "\n"

myFile.write(output)

myFile.close()
