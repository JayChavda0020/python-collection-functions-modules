''' Write a Python program to generate and print a list of first and last 5 elements where the values
are square of numbers between 1 and 30. '''

def printList(l):
    for i in range(1,31):
        i = (i**2)
        l.append(i)
    print(l[:5]+l[25:])
l = []
printList(l)