# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

d = {}

for key in range(1,16):
    d[key] = key*key

print(d)