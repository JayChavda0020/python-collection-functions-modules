# Write a Python program to print all unique values in a dictionary.

d = {"a":1, "b":2, "c":3, "d":2, "e":4, "f":3}

v = d.values()

s = list(set(v))

print(s)