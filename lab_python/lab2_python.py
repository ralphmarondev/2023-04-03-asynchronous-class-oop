# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# Write a program to input a string. Use the split() to separate the
# words in the string. Use also title(), len() and replace()
string = input("Enter string: ")

new_string = string.split(" ")
print(new_string)

print(string.title())
print(len(string))
print(string.replace("a", "b"))

