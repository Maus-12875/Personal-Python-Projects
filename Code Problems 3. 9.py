user_percentage = int(input("What was your percentage(no % needed)?"))
if user_percentage >= 90:
    print("You have scored an A")
elif 80 <= user_percentage <= 89:
    print("You have scored a B")
elif 70 <= user_percentage <= 79:
    print("You have scored a C")
elif 60 <= user_percentage <= 69:
    print("You have scored a D")
else: print("You have scored an F")
