# Write a Python program to convert a list to a tuple. 

list = ["P","y","t","h","o","n",1,2,3,True,False]

print(list)
print("*"*50)
print(tuple(list))

print("*"*50)
print((*list,))

print("*"*50)
tuple = ()
for i in list:
    tuple += (i,)
print(tuple)