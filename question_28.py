# Write a Python program to remove an empty tuple(s) from a list of tuples. 

l = [(1,2),(1,2,3,),(),(123,),()]

print(l)

for t in l :
    if len(t) == 0:
        l.remove(t)
print(l)