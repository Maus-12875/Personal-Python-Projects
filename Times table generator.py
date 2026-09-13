times_table = int(input("Which times table would you like to see? "))
max_value = int(input("How far would you like it to go to? "))
max_value = max_value + 1
answer = 0
print(f"Here is the {times_table} times table")
for x in range(1,max_value):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")
