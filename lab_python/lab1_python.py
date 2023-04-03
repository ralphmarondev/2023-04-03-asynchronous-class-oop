# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# Write a program to accept First name, Middle initial and Last name.
first_name = input("Enter first name: ")
middle_name = input("Enter middle name: ")
last_name = input("Enter last name: ")

my_list = []
for i in middle_name:
    my_list.append(i)

print(f"{first_name} {my_list[0]}. {last_name}")
