def SaveLogs(string,file):
    myFile = open(str(file),"w")
    myFile.write(str(string))
    myFile.close
    
string = str(input("What data do you want to store? "))
file = str(input("What is your filename? "))

SaveLogs(string,file)
