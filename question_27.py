# Write a Python program to find the repeated items of a tuple.

t = (10,2,3,4,5,6,4,1,0,10,56,10,5)
print(t)

e = int(input("Enter the value : "))
if e in t :
    c = t.count(e)
    print("No of", e, "in tuple is : ", c)
else:
    print(e, "is not in tuple")