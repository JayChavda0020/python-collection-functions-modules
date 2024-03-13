# Write a Python program to reverse a tuple. 

tuple = ("P","y","t","h","o","n",1,2,3,True,False)

print(tuple[::-1])

print("*"*50)

new_tuple = ()
for i in reversed(tuple):
    new_tuple += (i,)
print(new_tuple)

print("*"*50)

# rev_string = "".join(tuple)[::-1]
# rev_tuple = tuple(rev_string)
# print(rev_tuple)