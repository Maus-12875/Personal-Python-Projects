

# Selection (IF statements)

age  = int(input("How old are you? "))

if age > 17:
    print("You can legally vote")
else:
    print("your opinion is not valid!")

# Iteration (FOR and WHILE loops)

for i in range(10):
        print("Hello World!")

x = 0
while x < 10:
    print("Hello World!")
    x = x + 1

number = int(input("What is your number? "))

x = 1

while x < 13:
    print(str(number) + " x " + str(x) + " = " + str(number * x))
    x = x + 1

num = int(input("Which timestable do you want? "))

for i in range(1,13):
          answer = i * num
          print(str(i) + " x " + str(num) + " = " + str(answer))
