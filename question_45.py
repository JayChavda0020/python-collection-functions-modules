# Write a Python program to find the highest 3 values in a dictionary

d = {1:100, 2:500, 3:150, 4:1010, 5:50, 6:600}

l = list(d.values())
print(l)

l.sort()
print(l[-3:])