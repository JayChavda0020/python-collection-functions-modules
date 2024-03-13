# Write a Python program to convert a tuple to a string. 

tuple = ("P","y","t","h","o","n")

str = "".join(tuple)
print(str)

str1=""
for i in tuple:
    str1 += i 
print(str1)