# How will you compare two lists ?

l1 = [1,2,3,4,5]
l2 = [1,2,3,5,4]

l1.sort()
l2.sort()

if l1 == l2:
    print("list 1 and list 2 are same")
else:
    print("list 1 and list 2 are different")