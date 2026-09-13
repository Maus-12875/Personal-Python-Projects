def librarycode(title,year):
    parta = title[0:3]
    partb = year[2:]
    return(parta.upper + partb)

title = input("What is your title? ")
year = input("When was the book printed? ")
title = title.upper()


me = librarycode(title,year)

print(me)
