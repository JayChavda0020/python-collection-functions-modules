# Write a Python program to check whether an element exists within a tuple. 

''' def check(tuple):

    ele = input("Enter element to check : ")
    if ele in tuple:
        return True
    else:
        return False

tuple = ("P","y","t","h","o","n")    
print(check(tuple)) '''

tuple = ("P","y","t","h","o","n",1,2,3)

print(2 in tuple)
print("y" in tuple)
